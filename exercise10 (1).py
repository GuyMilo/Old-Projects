#!/usr/bin/env python
# coding: utf-8

# # Exercise 10

# Remember that a discrete dynamical system involves an $N\times N$ "transition" matrix $\mathbf{A}$ and an $N\times 1$ state vector $\mathbf{u}_k$ at time $k$:
# $$
# \begin{equation}
# \mathbf{u}_k = \mathbf{A}\mathbf{u}_{k-1} = \mathbf{A}^k\mathbf{u}_{0}
# \end{equation}
# $$
# given the $N^A \le N$ eigenvalues $\lambda_i$ and corresponding (orthonormal) eigenvectors $\mathbf{x}_i$ of the matrix $\mathbf{A}$, the initial state vector can be projected onto the eigenspace of $\mathbf{A}$:
# $$
# \begin{equation}
# \mathbf{u}^A_0 = proj(\mathbf{u}_0) = \sum_{i=1}^{N^A} a_i\mathbf{x}_{i}
# \end{equation}
# $$
# where $a_i$ are a set of $N^A$ constants and the eigenvectors of $\mathbf{A}$ do not necessarily need to span $\mathbb{R}^N$. Substituting the decomposed $\mathbf{u}_0$ into the original formulation:
# 
# \begin{equation}
# \mathbf{u}_k =  \mathbf{A}^k \mathbf{u}_{0} = \sum_{i=1}^{N^A} a_i\lambda^k \mathbf{x}_{i}
# \end{equation}
# 
# Create a Python module `dds.py` that uses the `numpy` and `matplotlib` modules to evaluate and visualize discrete dynamical systems. The module should contain the following functions:
# 
# * `eigendecompose(A, u0)` -- returns a tuple `(evals, evecs, consts)` where `evals` is the `list` of eigenvalues and `evecs` is the `list` ([$\mathbf{x}_1, \ \mathbf{x}_2, \ ..., \mathbf{x}_{N^A}$]) of eigenvectors of the `numpy` matrix `A` and `consts` is a `list` of constants $a_i$ from above for `u0`. Note that the eigenvectors should form an orthonormal set (if possible!).
# * `evaluate_decomposed(evals, evecs, consts, k)` -- *optimally* evaluates and returns an array $u_k$ given a list of eigenvalues, a list of eigenvectors, a list of constants, and $k$.
# * `evaluate(A, u0, k)` -- *optimally* evaluates and returns an array $u_k$ given an $N\times N$ transition matrix and $N\times 1$ initial state vector.
# * `evolution(A, u0, k)` -- returns an `numpy.ndarray` `U` with shape $(N, k+1)$ which contains each $u_k$ for $k=0\rightarrow k$ given an $N\times N$ transition matrix and $N\times 1$ initial state vector.
# * `plot(U, labels=None)` -- returns a `figure` object representing a single plot including each of the components of the state vectors contained in `U` with respect to step number ($k$). If `labels` is a `list` of $N$ strings, the figure should contain a legend with labels from the list.
# 
# All functions should check for valid input arguments and include appropriate doc-strings. If the input is invalid, the function should return `None`.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

def eigendecompose(A, u0):
    # Check if inputs are numpy arrays
    if not isinstance(A, np.ndarray) or not isinstance(u0, np.ndarray):
        print("Inputs must be numpy arrays.")
        return None

    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        print("Matrix must be square.")
        return None

    # Check if the matrix and vector have compatible dimensions
    if A.shape[0] != len(u0):
        print("Matrix and vector dimensions do not match.")
        return None

    # Compute eigenvalues and eigenvectors
    evals, evecs = np.linalg.eig(A)

    # Check if the matrix is diagonalizable (all eigenvalues are unique)
    if len(evals) != len(set(evals)):
        print("Matrix is not diagonalizable.")
        return None

    # Check if the eigenvectors can form a basis
    if np.linalg.matrix_rank(evecs) < len(u0):
        print("Eigenvectors cannot form a basis.")
        return None

    # Express u0 as a linear combination of the eigenvectors
    consts = np.linalg.solve(evecs.T, u0)

    return evals, evecs, consts

def evaluate_decomposed(evals, evecs, consts, k):
    # Check if inputs are numpy arrays
    if not all(isinstance(i, (list, np.ndarray)) for i in [evals, evecs, consts]) or not isinstance(k, int):
        print("Inputs must be numpy arrays.")
        return None

    # Check if k is a non-negative integer
    if not isinstance(k, int) or k < 0:
        print("k must be a non-negative integer.")
        return None

    # Check if the lengths of evals, evecs, and consts are equal
    if len(evals) != len(evecs) or len(evals) != len(consts):
        print("Inputs must have the same length.")
        return None

    # Check if the eigenvalues, eigenvectors, and constants are complex numbers
    if np.iscomplexobj(evals) or np.iscomplexobj(evecs) or np.iscomplexobj(consts):
        print("Inputs must not be complex numbers.")
        return None

    # Check if the eigenvectors are indeed vectors
    # for evec in evecs:
    #     if evec.shape != (len(evecs),):
    #         print("Eigenvectors must be vectors.")
    #         return None
        
    #Convert to numpy arrays for efficient calculation
    evals, evecs, consts = np.array(evals), np.array(evecs), np.array(consts)
    
    # Calculate the state vector at step k
    uk = sum(consts[i] * (evals[i] ** k) * evecs[i] for i in range(len(evals)))

    return uk

def evaluate(A, u0, k):
    # Check if inputs are numpy arrays
    if not isinstance(A, np.ndarray) or not isinstance(u0, np.ndarray):
        print("Inputs must be numpy arrays.")
        return None

    # Check if k is a non-negative integer
    if not isinstance(k, int) or k < 0:
        print("k must be a non-negative integer.")
        return None

    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        print("Matrix must be square.")
        return None

    # Check if the matrix and vector have compatible dimensions
    if A.shape[0] != len(u0):
        print("Matrix and vector dimensions do not match.")
        return None

    # Compute eigenvalues, eigenvectors, and constants
    result = eigendecompose(A, u0)
    
    if result is None:
        return None

    #evals, evecs, consts = result

    # Evaluate the state vector at step k
    uk = np.array(np.linalg.matrix_power(A, k).dot(u0))
    #uk = evaluate_decomposed(evals, evecs, consts, k)

    return uk

def evolution(A, u0, k):
    # Check if inputs are numpy arrays
    if not isinstance(A, np.ndarray) or not isinstance(u0, np.ndarray):
        print("Inputs must be numpy arrays.")
        return None

    # Check if k is a non-negative integer
    if not isinstance(k, int) or k < 0:
        print("k must be a non-negative integer.")
        return None

    # Check if the matrix is square
    if A.shape[0] != A.shape[1]:
        print("Matrix must be square.")
        return None

    # Check if the matrix and vector have compatible dimensions
    if A.shape[0] != len(u0):
        print("Matrix and vector dimensions do not match.")
        return None

    # Compute eigenvalues, eigenvectors, and constants
    result = eigendecompose(A, u0)
    
    if result is None:
        return None

    evals, evecs, consts = result

    # Initialize an empty array for the state vectors
    U = np.empty((len(u0), k+1))

    # Calculate the state vector at each step and add it to U
    for i in range(k+1):
        U[:, i] = evaluate_decomposed(evals, evecs, consts, i)

    return U

def plot(U, labels=None):
    # Check if U is a numpy array
    if not isinstance(U, np.ndarray):
        print("U must be a numpy array.")
        return None

    # Check if U is a 2D array
    if U.ndim != 2:
        print("U must be a 2D array.")
        return None

    # Check if labels is a list
    if labels is not None and not isinstance(labels, list):
        print("labels must be a list.")
        return None

    # Check if labels is a list of strings
    if labels is not None and not all(isinstance(label, str) for label in labels):
        print("labels must be a list of strings.")
        return None

    # Check if the number of labels matches the number of rows in U
    if labels is not None and len(labels) != U.shape[0]:
        print("The number of labels must match the number of rows in U.")
        return None

    # Create a new figure
    fig = plt.figure()

    # Plot each row of U
    for i in range(U.shape[0]):
        plt.plot(U[i], label=labels[i] if labels else None)

    # Add a legend if labels were provided
    if labels:
        plt.legend()

    return fig

