import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True)
    login = Column(String(250), nullable=False)
    save = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    planets = relationship('Planets')
    characters_id = Column(Integer, ForeignKey('Characters.id'))
    characters = relationship('characters')
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    favorites = relationship('Favorites')

class Planets(Base):
    __tablename__ = "Planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)
    cLimate = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    favorites = relationship('Favorites')
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User')

class Character(Base):
    __tablename__ = "Character"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    dob = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    favorites_id = Column(Integer, ForeignKey('Favorites.id'))
    favorites = relationship('Favorites')
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User')

class Favorites(Base):
    __tablename__ = "Favorites"
    id = Column(Integer, primary_key=True)
    characters_id = Column(Integer, ForeignKey('Characters.id'))
    characters = relationship('characters')
    planets_id = Column(Integer, ForeignKey('Planets.id'))
    planets = relationship('Planets')
    


    
    

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')