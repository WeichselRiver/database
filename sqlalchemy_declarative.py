# Use SQLALchemy declarative

import os
#import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from pydantic import BaseModel, constr, Field, ValidationError, validator
from typing import Pattern

 
 
Base = declarative_base()
 
class MarkeORM(Base):
    __tablename__ = 'marke'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)

class Marke(BaseModel):
    id: int
    name: constr(regex=r"^MichNr. [0-9]+$")

    class Config:
        orm_mode= True




class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    marke_id = Column(Integer, ForeignKey('marke.id'))
    marke = relationship(Marke)

# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
# engine = create_engine('postgresql://postgres:' + os.environ.get('DB_PASSWORD')+ '@localhost:5432/postgres')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.

# Base.metadata.create_all(engine)



try:
    p1_orm = MarkeORM( id = "123", name = "dMichNr. 1")
    p1 = Marke.from_orm(p1_orm)

    print(p1)

    
except ValidationError as e:
    print(e)




 