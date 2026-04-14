import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base


class AnomalyRecord(Base):
    __tablename__ = "anomaly_records"

    id = Column(Integer, primary_key=True, index=True)
    series_key = Column(String, nullable=False, index=True)
    anomaly_date = Column(String, nullable=True)
    anomaly_year = Column(Integer, nullable=True)
    observed_value = Column(Float, nullable=True)
    expected_value = Column(Float, nullable=True)
    anomaly_score = Column(Float, nullable=True)
    anomaly_type = Column(String, nullable=False)
    severity = Column(String, nullable=True)
    model_name = Column(String, nullable=True)
    explanation = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
