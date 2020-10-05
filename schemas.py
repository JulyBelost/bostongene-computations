from pydantic import BaseModel


class ComputationBase(BaseModel):
    value: int


class Computation(ComputationBase):
    id: int
    result: int = None

    class Config:
        orm_mode = True
