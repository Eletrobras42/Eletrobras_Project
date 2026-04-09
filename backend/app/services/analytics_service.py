import json
from statistics import mean, stdev
from typing import Optional

from app.models.sensor_data import SensorData
from app.models.prediction_log import PredictionLog


def safe_mean(values: list[float]) -> Optional[float]:
    return round(mean(values), 4) if values else None


def safe_stdev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    return stdev(values)


def parse_extra_data(raw_value: Optional[str]) -> dict:
    if not raw_value:
        return {}
    try:
        return json.loads(raw_value)
    except (ValueError, TypeError):
        return {}


def summarize_sensor_data(sensor_rows: list[SensorData]) -> dict:
    consumos = [row.consumo_kwh for row in sensor_rows]
    temperaturas = [row.temperatura for row in sensor_rows if row.temperatura is not None]
    producoes = [row.producao_hora for row in sensor_rows if row.producao_hora is not None]

    anomaly_count = 0
    if len(consumos) > 2:
        media = mean(consumos)
        sigma = safe_stdev(consumos)
        if sigma > 0:
            anomaly_count = sum(1 for value in consumos if abs(value - media) > 2 * sigma)

    production_efficiency = None
    production_pairs = [c / p for c, p in zip(consumos, producoes) if p and p > 0]
    if production_pairs:
        production_efficiency = round(mean(production_pairs), 4)

    return {
        "record_count": len(sensor_rows),
        "average_consumo_kwh": safe_mean(consumos) or 0.0,
        "min_consumo_kwh": round(min(consumos), 4) if consumos else 0.0,
        "max_consumo_kwh": round(max(consumos), 4) if consumos else 0.0,
        "average_temperature": safe_mean(temperaturas),
        "average_producao_hora": safe_mean(producoes),
        "production_efficiency": production_efficiency,
        "anomaly_count": anomaly_count,
        "extra_fields": parse_extra_data(sensor_rows[0].extra_data if sensor_rows else None),
    }


def summarize_predictions(predictions: list[PredictionLog]) -> dict:
    predicted_count = len(predictions)
    if predicted_count == 0:
        return {
            "prediction_count": 0,
            "tolerance_rate": 100.0,
            "last_prediction": None,
        }

    within_tolerance = sum(1 for p in predictions if not p.fora_tolerancia)
    last_prediction = max(predictions, key=lambda item: item.created_at)

    return {
        "prediction_count": predicted_count,
        "tolerance_rate": round(within_tolerance / predicted_count * 100, 2),
        "last_prediction": {
            "timestamp_min": last_prediction.timestamp_min,
            "predicted_consumo_kwh": last_prediction.predicted_consumo_kwh,
            "erro_percentual": last_prediction.erro_percentual,
            "fora_tolerancia": last_prediction.fora_tolerancia,
            "anomalia": last_prediction.anomalia,
            "created_at": last_prediction.created_at,
        },
    }


def summarize_dashboard_overview(sensor_rows: list[SensorData]) -> dict:
    if not sensor_rows:
        return {
            "machine_count": 0,
            "record_count": 0,
            "average_consumo_kwh": 0.0,
            "average_temperature": None,
            "average_producao_hora": None,
            "production_efficiency": None,
            "anomaly_rate": 0.0,
        }

    machines = set(row.machine_name for row in sensor_rows)
    consumos = [row.consumo_kwh for row in sensor_rows]
    temperaturas = [row.temperatura for row in sensor_rows if row.temperatura is not None]
    producoes = [row.producao_hora for row in sensor_rows if row.producao_hora is not None]

    production_pairs = [c / p for c, p in zip(consumos, producoes) if p and p > 0]
    efficiency = round(sum(production_pairs) / len(production_pairs), 4) if production_pairs else None

    anomaly_count = 0
    if len(consumos) > 1:
        mean_consumo = sum(consumos) / len(consumos)
        variance = sum((x - mean_consumo) ** 2 for x in consumos) / len(consumos)
        std = variance ** 0.5
        if std > 0:
            anomaly_count = sum(1 for value in consumos if abs(value - mean_consumo) > 2 * std)

    return {
        "machine_count": len(machines),
        "record_count": len(sensor_rows),
        "average_consumo_kwh": round(sum(consumos) / len(consumos), 4),
        "average_temperature": round(sum(temperaturas) / len(temperaturas), 4) if temperaturas else None,
        "average_producao_hora": round(sum(producoes) / len(producoes), 4) if producoes else None,
        "production_efficiency": efficiency,
        "anomaly_rate": round(anomaly_count / len(consumos) * 100, 2) if consumos else 0.0,
    }
