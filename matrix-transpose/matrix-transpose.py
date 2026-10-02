import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    N  = len(A)
    M = len(A[0])

    T = np.zeros((M,N), dtype = float)

    for i in range (N):
        for j in range(M):
            T[j][i] = A[i][j]

    return T
    
    pass
