from app.db.base import Base
from app.db.session import engine

# import models so they register with Base
from app.models import user, project, generation, usage, tenant


def init_db():
    Base.metadata.create_all(bind=engine)