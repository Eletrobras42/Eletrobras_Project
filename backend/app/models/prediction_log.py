import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from app.database.connection import Base


class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String, index=True, nullable=False)
    timestamp_min = Column(Integer, index=True, nullable=False)
    predicted_consumo_kwh = Column(Float, nullable=False)
    erro_percentual = Column(Float, nullable=False)
    fora_tolerancia = Column(Boolean, nullable=False)
    anomalia = Column(Boolean, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
