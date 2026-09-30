import numpy as np
import math 

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot = 0
    norm_a = 0
    norm_b = 0

    for i in range(len(a)):
        dot += a[i] * b[i]
        norm_a += a[i] ** 2
        norm_b += b[i] ** 2

    norm_a = math.sqrt(norm_a)
    norm_b = math.sqrt(norm_b)

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return float(dot/ (norm_a * norm_b))
    pass