from datetime import datetime

from app.services.interpolation_service import estimate_consumption
from app.services.metrics_service import calculate_error_and_tolerance
from app.services.anomaly_service import detect_anomaly
from app.repositories.sensor_data_repository import SensorDataRepository
from app.repositories.prediction_log_repository import PredictionLogRepository
from app.models.prediction_log import PredictionLog


def build_prediction(time_min: int, timestamps: list[int], consumos: list[float]) -> dict:
    predicted = estimate_consumption(time_min, timestamps, consumos)
    error_percentual, within_tolerance = calculate_error_and_tolerance(predicted, timestamps, consumos)
    anomaly = detect_anomaly(predicted, timestamps, consumos)

    return {
        "predicted_consumo_kwh": predicted,
        "erro_percentual": error_percentual,
        "fora_tolerancia": not within_tolerance,
        "anomalia": anomaly,
    }


class PredictionService:
    @staticmethod
    def interpolate_prediction(request, db):
        sensor_repo = SensorDataRepository(db)
        prediction_repo = PredictionLogRepository(db)

        sensor_rows = sensor_repo.get_by_machine(request.machine)
        if len(sensor_rows) < 2:
            return None

        prediction = build_prediction(
            request.time,
            [row.timestamp_min for row in sensor_rows],
            [row.consumo_kwh for row in sensor_rows],
        )

        log = PredictionLog(
            machine_name=request.machine,
            timestamp_min=request.time,
            predicted_consumo_kwh=prediction["predicted_consumo_kwh"],
            erro_percentual=prediction["erro_percentual"],
            fora_tolerancia=prediction["fora_tolerancia"],
            anomalia=prediction["anomalia"],
            created_at=datetime.utcnow(),
        )
        prediction_repo.create(log)

        temperature_values = [row.temperatura for row in sensor_rows if row.temperatura is not None]
        production_values = [row.producao_hora for row in sensor_rows if row.producao_hora is not None]

        average_temperature = round(sum(temperature_values) / len(temperature_values), 2) if temperature_values else None
        average_producao_hora = round(sum(production_values) / len(production_values), 2) if production_values else None

        return {
            "machine": request.machine,
            "time": request.time,
            "consumo_estimado": prediction["predicted_consumo_kwh"],
            "erro_percentual": prediction["erro_percentual"],
            "fora_tolerancia": prediction["fora_tolerancia"],
            "anomalia": prediction["anomalia"],
            "history_count": len(sensor_rows),
            "worker_activity_min": request.worker_activity_min,
            "average_temperature": average_temperature,
            "average_producao_hora": average_producao_hora,
        }
