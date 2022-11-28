import uvicorn
from typing import List
from sqlalchemy.orm import Session
from models import hf_data, schemas
from db.database import engine, get_db
from fastapi import FastAPI, Depends, status, Request, Form

app = FastAPI()  # initialize fastapi instance
#Create the database
hf_data.Base.metadata.create_all(engine)  # create all sql tables (empty) if they don't exist

@app.get("/records/", response_model=List[schemas.Record])
def show_records(db: Session = Depends(get_db)):
    records = db.query(hf_data.RottenTomatoes).limit(5).all()
    return records

@app.get('/query_substring/{substring}', response_model=List[schemas.Record])
def query_substring(substring, db: Session = Depends(get_db)):
    records = db.query(hf_data.RottenTomatoes).filter(hf_data.RottenTomatoes.text.like('%' + substring + '%')).limit(5).all()
    return records

if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=False, root_path="/")