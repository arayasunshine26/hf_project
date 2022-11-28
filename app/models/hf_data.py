import uuid
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class RottenTomatoes(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'RottenTomatoes'
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(String, primary_key=True, nullable=False, default=generate_uuid)
    text = Column(String)
    label = Column(Integer)