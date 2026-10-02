from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # mean 
    mean = sum(x)/len(x)

    # median
    sorted_data = sorted(x)
    n = len(x)

    if n % 2 == 1:
        median = sorted_data[n//2]
    else:
        median = (sorted_data[n//2-1] + sorted_data[n//2]) /2

    # mode
    counts = Counter(x)
    max_count = max(counts.values())
    mode = min(x for x, count in counts.items() if count == max_count)

    return {
        "mean": float(mean),
        "median": float(median),
        "mode": float(mode) 
    }
 
    pass