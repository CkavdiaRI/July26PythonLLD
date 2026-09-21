# Python code -> SQLAlchemy -> SQL -> PyMysql -> MySQL

# SQLAlchemy is an Object Relational Mapper (ORM) that allows developers 
# to interact with databases using Python classes and objects instead of\
# writing raw SQL queries. It provides a high-level abstraction for database 
# operations, making it easier to work with relational databases like MySQL.

# PyMySQL is a pure-Python MySQL client library that allows Python applications
# to connect to MySQL databases. It provides a way to execute SQL queries and
# manage database connections in a Pythonic way.

# MySQL is a popular open-source relational database management system (RDBMS)

import datetime
from sqlalchemy import declarative_base
from sqlalchemy import Column, Integer, DateTime

# InSQLAlchemy, a class becomes a real table simply by inheriting from a special base class
# and declaring a __tablename_- attribute. 
Base = declarative_base()

class BaseModel:
    __abstract__ = True  # This class is abstract and should not be instantiated directly

    # def __init__(self):
    #     self.id = None 
    #     self.created_at = datetime.now()  
    #     self.updated_at = datetime.now()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    