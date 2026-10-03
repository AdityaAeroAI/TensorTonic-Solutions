import numpy as np
import math
def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    mean = sum(x) / n
    
    squared_deviations = [(value - mean) ** 2 for value in x]

    variance = sum(squared_deviations) / (n-1)
    standard_deviation = math.sqrt(variance)

    return {
        "variance": float(variance),
        "standard_deviation": float(standard_deviation)
    }
    pass