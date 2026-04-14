from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db() -> None:
    from app.models.source_document import SourceDocument
    from app.models.ingestion_run import IngestionRun
    from app.models.reported_indicator import ReportedIndicator
    from app.models.indicator_series import IndicatorSeries
    from app.models.interpolation_record import InterpolationRecord
    from app.models.anomaly_record import AnomalyRecord
    from app.models.dashboard_snapshot import DashboardSnapshot
    from app.models.sensor_data import SensorData
    from app.models.prediction_log import PredictionLog

    Base.metadata.create_all(bind=engine)
