from sqlalchemy import Column, Integer, Float, Sequence
from db import Base


class Computation(Base):
    __tablename__ = "computations"

    id = Column(Integer, Sequence("seq1"), primary_key=True)
    value = Column(Float)
    result = Column(Float)

    def __init__(self, value):
        self.value = value
