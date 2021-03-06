#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This class defines users"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship('Place',
                          backref="user",
                          cascade="all, delete, delete-orphan")

    reviews = relationship('Review',
                           backref="user",
                           cascade="all, delete, delete-orphan")
