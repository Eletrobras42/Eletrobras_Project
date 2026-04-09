import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_FILE = os.path.join(os.path.dirname(__file__), "eletrobras.db")
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    from app.models.sensor_data import SensorData
    from app.models.prediction_log import PredictionLog

    Base.metadata.create_all(bind=engine)
