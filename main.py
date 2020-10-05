import asyncio

from sqlalchemy.orm import Session
from fastapi import FastAPI
from fastapi import Depends
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


async def compute(value, id_):
    session = db.SessionLocal()
    db_computation = session.query(models.Computation).get(id_)

    setattr(db_computation, "result", value * 2)

    session.commit()
    session.refresh(db_computation)


@app.get(
    "/result/{id_}",
)
async def get_computation(id_: int, session: Session = Depends(get_session)):
    computation = session.query(models.Computation).get(id_)

    return computation.result


@app.get(
    "/calculate/{value}",
)
async def start_computation(value: int, session: Session = Depends(get_session)):
    new_computation = models.Computation(value=value)
    session.add(new_computation)
    session.commit()
    session.refresh(new_computation)

    asyncio.create_task(compute(value, new_computation.id))

    return new_computation.id
