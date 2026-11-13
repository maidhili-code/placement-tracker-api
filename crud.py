
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Application


def create_application(db: Session, data, user_id: int):
    app = Application(
        **data.model_dump(),
        user_id=user_id
    )
    db.add(app)
    db.commit()
    db.refresh(app)
    return app


def get_applications(db: Session, user_id: int):
    query = select(Application).where(
        Application.user_id == user_id
    )
    return list(db.scalars(query).all())


def get_application(db: Session, app_id: int, user_id: int):
    query = select(Application).where(
        Application.app_id == app_id,
        Application.user_id == user_id
    )
    return db.scalars(query).first()


def update_application(db: Session, app_id: int, data, user_id: int):
    app = get_application(db, app_id, user_id)

    if app is None:
        return None

    for key, value in data.model_dump().items():
        setattr(app, key, value)

    db.commit()
    db.refresh(app)
    return app


def patch_application(db: Session, app_id: int, data, user_id: int):
    app = get_application(db, app_id, user_id)

    if app is None:
        return None

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(app, key, value)

    db.commit()
    db.refresh(app)
    return app


def delete_application(db: Session, app_id: int, user_id: int):
    app = get_application(db, app_id, user_id)

    if app is None:
        return False

    db.delete(app)
    db.commit()
    return True
