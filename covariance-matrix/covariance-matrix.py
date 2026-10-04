import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    X = np.array(X, dtype = float)

    N = X.shape[0]

    mean = np.mean(X, axis = 0)

    Xc = X - mean

    covariance = (Xc.T @ Xc) / (N -1)

    return covariance

    pass