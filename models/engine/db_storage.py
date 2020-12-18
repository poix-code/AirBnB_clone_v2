#!/usr/bin/python3
"""Module to manage a database"""
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv


classes = {'State': State, 'City': City, 'User': User,
           'Place': Place, 'Review': Review}


class DBStorage:
    """Private class attributes"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes variables"""
        usr = getenv('HBNB_MYSQL_USER')
        psw = getenv('HBNB_MYSQL_PWD')
        hst = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(usr,
                                                                           psw,
                                                                           hst,
                                                                           db),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)"""
        session = self.__session
        data = {}
        if cls and cls in classes.values():
            log = session.query(cls).all()
            for obj in log:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                value = obj
                data[key] = value
        elif cls is None:
            for val in classes.values():
                log = session.query(val).all()
                for obj in log:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    value = obj
                    data[key] = value
        return data

    def new(self, obj):
        """add a object to the database selected in the session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes in the database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """If the object is not None is deleted of the database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
