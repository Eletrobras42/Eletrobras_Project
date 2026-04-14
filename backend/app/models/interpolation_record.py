import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from app.core.database import Base


class InterpolationRecord(Base):
    __tablename__ = "interpolation_records"

    id = Column(Integer, primary_key=True, index=True)
    series_key = Column(String, nullable=False, index=True)
    reference_point_before = Column(String, nullable=True)
    reference_point_after = Column(String, nullable=True)
    target_observation_date = Column(String, nullable=False)
    target_observation_year = Column(Integer, nullable=True)
    interpolated_value = Column(Float, nullable=False)
    method_name = Column(String, nullable=False)
    source_context = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
