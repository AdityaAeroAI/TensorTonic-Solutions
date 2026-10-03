import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    total = 0

    for x, p in zip (x, p):
        total += x * p

    return float(total)
    pass