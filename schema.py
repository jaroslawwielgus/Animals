from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
connection_string = "sqlite:///" + os.path.join(BASE_DIR, 'animals.db')

Base = declarative_base()
engine = create_engine(connection_string, echo=True)
Session = sessionmaker()

'''Creating schema classes for each animal class'''
class Cat(Base):
    __tablename__ = 'cats'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    isCatchingMouses = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f"Race: {self.race}"

#cat1 = Cat(race='kot sfinks', color='zróżnicowane', height=0.28, weight=4.5, length_of_life=13.5, isWild=False, isCatchingMouses=False)
#print(cat1)

class Dog(Base):
    __tablename__ = 'dogs'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    isRetrieving = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f"Race: {self.race} Color: {self.color}"


class Cow(Base):
    __tablename__ = 'cows'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    isGivingMilk = Column(Boolean(), nullable=False)
    isForMeat = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f"Race: {self.race} Color: {self.color}"


class Horse(Base):
    __tablename__ = 'horses'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    isDraught = Column(Boolean(), nullable=False)
    isSports = Column(Boolean(), nullable=False)
    mane = Column(String(30), nullable=False)

    def __repr__(self):
        return f"Race: {self.race} Color: {self.color}"


class Lion(Base):
    __tablename__ = 'lions'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    mane = Column(String(30), nullable=False)

    def __repr__(self):
        return f"Race: {self.race} Color: {self.color}"


class Canary(Base):
    __tablename__ = 'canaries'
    id = Column(Integer(), primary_key=True)
    race = Column(String(30), nullable=False, unique=True)
    color = Column(String(30), nullable=False)
    height = Column(Float(2), nullable=False)
    weight = Column(Float(2), nullable=False)
    length_of_life = Column(Float(1), nullable=False)
    isWild = Column(Boolean(), nullable=False)
    isHavingMane = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f"Race: {self.race} Color: {self.color}"