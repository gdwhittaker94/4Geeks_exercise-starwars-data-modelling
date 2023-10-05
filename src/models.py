import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = name = Column(String(50), nullable=False)
    country = Column(String(50))
    birthday = Column(String(50))
    email = Column(String(50), unique=True)
    fav_user_Planets = relationship('Favorite_Planets', backref='users', lazy=True)
    fav_user_Characters = relationship('Favorite_Characters', backref='users', lazy=True)
    fav_user_Vehicles = relationship('Favorite_Vehicles', backref='users', lazy=True)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    model = Column(String(50))
    vehicle_class = Column(String(50))
    manufacturer = Column(String(50))
    consumables = Column(String(50))
    cost_in_credits = Column(Integer)
    crew = Column(Integer)
    length = Column(Float)
    crew = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    population = Column(Integer)
    surface_water = Column(Integer)
    name = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))
    fav_planet = relationship('Favorite_planets', backref='planets', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    gender = Column(String(50))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))

    
class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class Favorite_Characters(Base):
    __tablename__ = 'favorite_characters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

class Favorite_Vehicles(Base):
    __tablename__ = 'favorite_vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

  
# def to_dict(self):
#     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')


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