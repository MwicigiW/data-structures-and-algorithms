'''
What are data structures and algorithms?
  - Data structure = systematic way of organizing and accessing data
  - Algorithm = step-by-step procedure for performing some task in a finite amount of time. 
  
To analyze how "good" these things are, we use running time and space, since both are precious resources.

Since various factors affect runtime (CPU power, temperature, etc.) we use the relative running time O(n), 
with n being the number of inputs.

For simplicity, we will always assume worst-case time.

'''
def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n  # create new list of n zeros
    for j in range(n):
        total = 0  # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j + 1)  # record the average
    return A

'''
Functions
Constant = (O)1
Logarithmic = (O)log n 
Linear = n
N-Log-N = 
Quadratic = n^2
  - Nested Loops
  - Summations
Cubic & Polynomials
Exponentials
  - Geometric Sums

Big O notation
Big Omega
Big Theta

Justification Techniques
  - By Example
  - Contra Attack
  - Induction and Loop Invariants
  - 
  


