FROM python:3.7

WORKDIR /bostongene_computations

RUN pip install fastapi fastapi-sqlalchemy pydantic psycopg2 uvicorn

COPY . /bostongene_computations

EXPOSE 8000
