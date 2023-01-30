import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base

DSN = 'postgresql://postgres:postgres@localhost:5432/bookstore'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session

