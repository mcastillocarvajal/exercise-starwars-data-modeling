import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(15), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorite_character = relationship('Favorite_Character', uselist=False, back_populates='user')
    favorite_planet = relationship('Favorite_Planet', uselist=False, back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    gender = Column(String(30))
    height = Column(Integer)
    birth_year = Column(String(15))
    mass = Column(Integer)
    hair_color = Column(String(15))
    skin_color = Column(String(15))
    eye_color = Column(String(15))
    favorite_character = relationship('Favorite_Character', uselist=False, back_populates='character')

class Favorite_Character(Base):
    __tablename__ = 'favorite_character'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship('Character', back_populates='favorite_character')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    climate = Column(String(30))
    diameter = Column(Integer)
    gravity = Column(String(15))
    terrain = Column(String(15))
    surface_water = Column(Integer)
    population = Column(Integer)
    favorite_planet = relationship('Favorite_Planet', uselist=False, back_populates='planet')

class Favorite_Planet(Base):
    __tablename__ = 'favorite_planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet', back_populates='favorite_planet')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')