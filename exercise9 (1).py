#!/usr/bin/env python
# coding: utf-8

# # Exercise 9

# In[ ]:


# Execute this code block to import the NumPy library
import numpy as np


# #### Problem 1
# 
# Using `NumPy`'s linear algebra module, develop a function `problem1(A,b)` that returns `True` if the linear equation system $\mathbf{Ax} = \mathbf{b}$ has a unique solution and `False` otherwise.

# In[1]:

def problem1(A, b):
    #Check if A is a square matrix and
    #if the dimensions of b match A
    if A.shape[0] == A.shape[1] and A.shape[0] == b.shape[0]:
        try:
            det = np.linalg.det(A)
            if det != 0:
                return True
            else:
                return False
        except np.linalg.LinAlgError:
            return False
    else:
        print("Error: The matrix A must be square and the dimensions of b must ")
        return False
"""
The key to this problem is understanding that a system
of linear equations has a unique solution if and only 
if the determinant of the matrix A is non-zero. If the 
determinant is zero, the system has either no solutions 
or infinitely many solutions. Here's how you could implement 
this in Python using NumPy:

This function first tries to calculate the determinant of A.
If A is not square or if any other error occurs during the 
calculation, np.linalg.det() will raise a LinAlgError. 
The function catches this exception and returns False. 
If the determinant is calculated successfully, the function 
checks if it is non-zero and returns True or False accordingly. 

In this version of the function, we first check if A is a 
square matrix (A.shape[0] == A.shape[1]) and if the dimensions 
of b match A (A.shape[0] == b.shape[0]). If either condition 
is not met, we print an error message and return False.
"""


# #### Problem 2
# 
# Using `NumPy`'s linear algebra module and your solution to Problem 1, develop a function `problem2(A,b,method)` that returns the elapsed time (seconds) required to solve the linear equation system $\mathbf{Ax} = \mathbf{b}$ using (i) Gaussian Elimination if `method = "ge"` (`linalg.solve()`) or (ii) the inverse ($\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$) method if `method = "inv"`. If the linear equation system does not have a unique solution or is not solvable, return `None`.

# In[ ]:


import time

def problem2(A, b, method):
    
    
    if np.linalg.matrix_rank(A) == min(A.shape):
        if problem1(A, b): # Check if the system has a unique solution
            start_time = time.time() # Start the timer
            if method == "ge":
                np.linalg.solve(A, b) # Gaussian Elimination
            elif method == "inv":
                np.linalg.inv(A).dot(b) #Inverse Method 
            else:
                return None
            end_time = time.time() #Stop the timer
            return end_time - start_time #Return elapsed time
        else:
            return None
    else:
        print("Error: The matrix A must be of full rank.")
        return None



# #### Problem 3
# 
# Use the `NumPy` functions `polyfit()`, `random.random()`, and your solution to Problem 2 to develop a function `problem3(n_array, method)` that returns a `array` of the coefficients of the best-fit polynomial $t(n)$ for the runtime of Gaussian elimination or the inverse matrix method depending on the value of `method` (`"ge"` or `"inv"`). The runtime should be fit to a third order polynomial:
# 
# $t(n) = a_0 + a_1 n + a_2 n^2 + a_3 n^3$
# 
# where $t(n)$ is the runtime of the method for solving a linear system of size $n$. The input argument `n_array` specifies the dimensions of the linear systems that should be used as a sample set to measure runtimes which are then used to determine a best-fit. The best fit $t(n)$ provides us with an approximation of the runtime versus linear system size for the specified method (`"ge"` or `"inv"`).
# 
# The `random.random()` function should be used to generate the linear equation systems of different dimensions (specified by `n_array`) which, in turn, will be used to create timing data points $(n, t)$ for fitting to the polynomial.

# In[ ]:


def problem3(n_array, method):
    #Initialize arrays to store n values and corresponding times
    n_values = []
    times = []

    #for each n in n_array
    for n in n_array:
        #Generate a random nxn matrix A
        A = np.random.random((n,n))
        b = np.random.random((n,1))

        #Measure the time taken to solve the system
        time_taken = problem2(A, b, method)

        #If the system was solvable, store n and the time taken
        if time_taken is not None:
            n_values.append(n)
            times.append(time_taken)
    
    #Fit a third degree polynomial to the data and return 
    #the coefficients
    return np.polyfit(n_values, times, 3)


"""
This function will return an array of four coefficients, 
[a3, a2, a1, a0], representing the best-fit polynomial 
a3 * n**3 + a2 * n**2 + a1 * n + a0.
"""

