from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import hf_data
from models.hf_data import RottenTomatoes
import pandas as pd
import uuid

SQLALCHEMY_DATABASE_URL = 'sqlite:///db/hf_data.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        Base.metadata.create_all(engine)
        file_name = 'data/rotten_tomatoes.csv'
        df = pd.read_csv(file_name)
        df.to_sql(con=engine, index_label='id', name=RottenTomatoes.__tablename__, if_exists='replace')
        yield db
    finally:
        db.close()