"""Import statistics; an empty import has average zero."""


def average(values: list[float]) -> float:
    return sum(values) / len(values)
