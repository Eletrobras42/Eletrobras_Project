import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from app.core.database import Base


class IndicatorSeries(Base):
    __tablename__ = "indicator_series"

    id = Column(Integer, primary_key=True, index=True)
    series_key = Column(String, nullable=False, index=True)
    indicator_name = Column(String, nullable=False)
    indicator_category = Column(String, nullable=True)
    metric_unit = Column(String, nullable=True)
    observation_year = Column(Integer, nullable=False, index=True)
    observation_date = Column(String, nullable=True)
    numeric_value = Column(Float, nullable=True)
    source_document_id = Column(Integer, ForeignKey("source_documents.id"), nullable=True)
    reported_indicator_id = Column(Integer, ForeignKey("reported_indicators.id"), nullable=True)
    is_interpolated = Column(Integer, nullable=False, default=0)
    interpolation_method = Column(String, nullable=True)
    confidence_score = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
