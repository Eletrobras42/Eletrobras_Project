import numpy as np
from scipy.interpolate import interp1d


def estimate_consumption(time_min: int, times: list[int], consumos: list[float]) -> float:
    if len(times) < 2:
        raise ValueError("Pelo menos dois pontos são necessários para interpolação")

    x = np.array(times, dtype=float)
    y = np.array(consumos, dtype=float)
    interpolator = interp1d(x, y, kind="linear", fill_value="extrapolate", bounds_error=False)
    resultado = float(interpolator(float(time_min)))
    return round(resultado, 4)
