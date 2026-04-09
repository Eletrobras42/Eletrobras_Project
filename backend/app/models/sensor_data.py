import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database.connection import Base


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    machine_name = Column(String, index=True, nullable=False)
    timestamp_min = Column(Integer, index=True, nullable=False)
    consumo_kwh = Column(Float, nullable=False)
    temperatura = Column(Float, nullable=True)
    producao_hora = Column(Float, nullable=True)
    worker_activity_min = Column(Integer, nullable=True)
    status = Column(String, nullable=True)
    extra_data = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
