#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models.engine.file_storage import FileStorage
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """returns the list of City instances with
            state_id equals to the current State.id"""
            obj = models.storage.all(City)
            data = []
            for city in obj.values():
                if city.state_id == self.id:
                    data.append(city)
            return data

    def __init__(self, *args, **kwargs):
        """calling state init"""
        super().__init__(*args, **kwargs)
