import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    username = Column(String(20), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('usuario.id'))
    person = relationship(Usuario)

class Personajes(Base):
    __tablename__ = 'personajes'   
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    person_class = Column(String(250))
    faccion = Column(String(250))
    race = Column(String(250))
    gender = Column(String(250), nullable=False )

class Planetas(Base):
    __tablename__ = 'planetas'   
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    size = Column(String(250))
    temp = Column(Integer)
    color = Column(String)
    moon_numbers = Column(String(250))

class Vehicles(Base):
    __tablename__ = 'vehicles'  
    id = Column(Integer, primary_key=True)
    type_vehicle = Column(String(250))
    color = Column(String(250))
    model = Column(String(250))
    brand = Column(String(250))
    price = Column(Float(2))
    passengers = Column(Integer)

class Favorites(Base):
    __tablename__ = 'favorites'  
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    vehicle_favorites = relationship(Vehicles)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=True)
    usuario_favorites = relationship(Usuario)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    personaje_favorites = relationship(Personajes)
    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    planeta_favorites = relationship(Planetas)    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
