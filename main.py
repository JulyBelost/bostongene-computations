from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi import Depends, Response
from starlette import status

import db
import models

app = FastAPI(title="Boston Gene test task")

metadata = db.Base.metadata
metadata.create_all(db.engine)


def get_session():
    session = db.SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get(
    "/result/{id_}",
    status_code=status.HTTP_201_CREATED
)
async def get_computation(id_: int, response: Response, session: Session = Depends(get_session)):
    computation = session.query(models.Computation).get(id_)

    if computation.result:
        response.status_code = status.HTTP_200_OK
        return computation.result


@app.get(
    "/calculate/{value}",
    status_code=status.HTTP_201_CREATED
)
async def start_computation(value: int, session: Session = Depends(get_session)):
    new_computation = models.Computation(value=value)
    session.add(new_computation)
    session.commit()
    session.refresh(new_computation)

    return new_computation.id
