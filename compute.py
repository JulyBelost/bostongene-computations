from time import sleep

import db
from models import Computation


def compute(id_):
    session = db.SessionLocal()

    db_computation = session.query(Computation).get(id_)

    setattr(db_computation, "result", db_computation.value * 2)

    session.commit()
    session.refresh(db_computation)


if __name__ == '__main__':
    session_main = db.SessionLocal()

    while True:
        ids = session_main.query(Computation.id).filter(Computation.result == None).all()
        for x in ids:
            print(x)
            compute(x)

        sleep(10)
