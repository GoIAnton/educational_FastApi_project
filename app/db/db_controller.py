import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from custom_exceptions import NoEnvironmentVariableException
import db.models as db


try:
    url = os.getenv('DATABASE_URL')
    if url is None:
        raise NoEnvironmentVariableException('DATABASE_URL')
    engine = create_engine(
        url,
        echo=True
    )
except NoEnvironmentVariableException as e:
    print(e)


db.Base.metadata.create_all(engine)
