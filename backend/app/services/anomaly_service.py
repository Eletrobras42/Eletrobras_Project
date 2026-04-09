import numpy as np


def detect_anomaly(predicted: float, times: list[int], consumos: list[float]) -> bool:
    if len(consumos) < 3:
        return False

    mean = float(np.mean(consumos))
    std = float(np.std(consumos))
    if std == 0:
        return False

    return abs(predicted - mean) > 2 * std
