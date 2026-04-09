from app.services.interpolation_service import estimate_consumption
from app.services.metrics_service import calculate_error_and_tolerance
from app.services.anomaly_service import detect_anomaly


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
