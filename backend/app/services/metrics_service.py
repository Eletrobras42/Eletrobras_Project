def calculate_error_and_tolerance(predicted: float, times: list[int], consumos: list[float]) -> tuple[float, bool]:
    if not consumos:
        return 0.0, True

    reference = consumos[-1]
    if reference == 0:
        return 0.0, True

    error = abs(predicted - reference) / reference * 100
    tolerance_percentage = 10.0
    return round(error, 2), error <= tolerance_percentage
