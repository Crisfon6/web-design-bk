from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from environment.constants import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB ,DATABASE_HOST,DATABASE_PORT

URL_DATABASE = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_HOST}:${DATABASE_PORT}/{POSTGRES_DB}'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()