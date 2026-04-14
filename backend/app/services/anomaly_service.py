import numpy as np


def detect_anomaly(predicted: float, times: list[int], consumos: list[float]) -> bool:
    if len(consumos) < 3:
        return False

    mean = float(np.mean(consumos))
    std = float(np.std(consumos))
    if std == 0:
        return False

    return abs(predicted - mean) > 2 * std


class AnomalyService:
    @staticmethod
    def list_anomalies(db):
        from app.repositories.anomaly_repository import AnomalyRepository

        repository = AnomalyRepository(db)
        records = repository.get_all()
        return [
            {
                "series_key": row.series_key,
                "anomaly_date": row.anomaly_date,
                "anomaly_year": row.anomaly_year,
                "observed_value": row.observed_value,
                "expected_value": row.expected_value,
                "anomaly_score": row.anomaly_score,
                "anomaly_type": row.anomaly_type,
                "severity": row.severity,
                "model_name": row.model_name,
                "explanation": row.explanation,
            }
            for row in records
        ]
