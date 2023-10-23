from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

engine = create_engine('sqlite:///star_wars.db')

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    birth_year = Column(String, unique=True)
    eye_color = Column(BigInteger)
    gender = Column(String)
    hair_color = Column(String)
    height = Column(Integer)
    homeworld = Column(String)
    mass = Column(Integer)
    skin_color = Column(String)

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True, autoincrement=True)
    film_id = Column(Integer)
    person_id = Column(Integer, ForeignKey(Person.id))


class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True, autoincrement=True)
    specie_id = Column(Integer)
    person_id = Column(Integer, ForeignKey(Person.id))
class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True, autoincrement=True)
    starship_id = Column(Integer)
    person_id = Column(Integer, ForeignKey(Person.id))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    vehicles_id = Column(Integer)
    person_id = Column(Integer, ForeignKey(Person.id))

Base.metadata.create_all(bind=engine)
