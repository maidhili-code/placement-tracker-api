from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from schemas import (
    ApplicationCreate, ApplicationUpdate,
    ApplicationPatch, ApplicationResponse,
)
import models
import crud
from fastapi.security import OAuth2PasswordRequestForm
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)
from schemas import UserCreate, UserResponse, Token
from auth import get_current_user

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Job Tracker")

def or_404(result):
    if result is None:
        raise HTTPException(status_code=404, detail="application not found")
    return result

@app.get("/")
def home():
    return {"message": "welcome to job tracker"}


@app.post("/applications", response_model=ApplicationResponse, status_code=201)
def create(
    data: ApplicationCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.create_application(db, data, current_user.id)


@app.get("/applications", response_model=list[ApplicationResponse])
def read_all(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return crud.get_applications(db, current_user.id)


@app.get("/applications/{app_id}", response_model=ApplicationResponse)
def read_one(
    app_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return or_404(
        crud.get_application(db, app_id, current_user.id)
    )


@app.put("/applications/{app_id}", response_model=ApplicationResponse)
def update(
    app_id: int,
    data: ApplicationUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return or_404(
        crud.update_application(db, app_id, data, current_user.id)
    )


@app.patch("/applications/{app_id}", response_model=ApplicationResponse)
def patch(
    app_id: int,
    data: ApplicationPatch,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return or_404(
        crud.patch_application(db, app_id, data, current_user.id)
    )


@app.delete("/applications/{app_id}")
def delete(
    app_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    if not crud.delete_application(db, app_id, current_user.id):
        raise HTTPException(status_code=404, detail="Application not found")

    return {"message": "Application deleted successfully"}


@app.post("/register", response_model=UserResponse, status_code=201)
def register(data: UserCreate, db: Session = Depends(get_db)):

    existing = db.query(models.User).filter(
        (models.User.username == data.username) |
        (models.User.email == data.email)
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Username or email already exists"
        )

    user = models.User(
        username=data.username,
        email=data.email,
        hashed_password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@app.post("/login", response_model=Token)
def login(
    form: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.username == form.username
    ).first()

    if not user or not verify_password(
        form.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(user.id)

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@app.get("/profile", response_model=UserResponse)
def profile(
    current_user=Depends(get_current_user)
):
    return current_user
