"""Import statistics; an empty import has average zero."""


def average(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)
