from sqlalchemy.orm import Session

from app.repositories.anomaly_repository import AnomalyRepository
from app.repositories.source_repository import SourceDocumentRepository
from app.repositories.reported_indicator_repository import ReportedIndicatorRepository
from app.repositories.indicator_series_repository import IndicatorSeriesRepository
from app.repositories.ingestion_run_repository import IngestionRunRepository


class KpiService:
    @staticmethod
    def get_kpis(db: Session):
        source_repo = SourceDocumentRepository(db)
        indicator_repo = ReportedIndicatorRepository(db)
        series_repo = IndicatorSeriesRepository(db)
        anomaly_repo = AnomalyRepository(db)
        ingestion_repo = IngestionRunRepository(db)

        return {
            "documents_cataloged": len(source_repo.get_all()),
            "indicators_extracted": len(indicator_repo.get_all()),
            "series_consolidated": len(series_repo.get_all()),
            "anomalies_detected": len(anomaly_repo.get_all()),
            "ingestion_runs": len(ingestion_repo.get_all()),
        }
