from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound


def get_or_create(session, model, **kwargs):
    try:
        return model.query.filter_by(**kwargs).one()
    except NoResultFound:
        return create_model(session, model, **kwargs)


def create_model(session, model, **kwargs):
    created = model(**kwargs)
    try:
        session.add(created)
        session.commit()
        return created
    except IntegrityError:
        session.rollback()
        return session.query(model).filter_by(**kwargs).one()
