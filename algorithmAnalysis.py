'''
What are data structures and algorithms?
  - Data structure = systematic way of organizing and accessing data
  - Algorithm = step-by-step procedure for performing some task in a finite amount of time. 
  
To analyze how "good" these things are, we use running time and space, since both are precious resources.

Since various factors affect runtime (CPU power, temperature, etc.) we use the relative running time O(n), 
with n being the number of inputs.

For simplicity, we will always assume worst-case time.

Functions

Constant = (O)1
  - Accessing an element at a particular index of a list
  
    '''
    def get_element_at_index(lst, index):
      """Return the element at the specified index in the list."""
      return lst[index]
  '''
  
Logarithmic = (O)log n
  - Binary search, constantly halving until you find it
  
    '''
    def binary_search(arr, target):
      """Perform binary search on a sorted list and return the index of the target element."""
      low = 0
      high = len(arr) - 1

      while low <= high:
          mid = (low + high) // 2
          mid_value = arr[mid]

          if mid_value == target:
              return mid
          elif mid_value < target:
              low = mid + 1
          else:
              high = mid - 1

      return -1  # Target element not found
  '''
  
Linear = n
  - Linear search. Iterate over any index of a set
  
    '''
    def linear_search(arr, target):
      """Perform linear search on a list and return the index of the target element."""
      for i in range(len(arr)):
          if arr[i] == target:
              return i

      return -1  # Target element not found
  '''

N-Log-N = 
  - Merge Sort
  
    ''' 
    def merge_sort(arr):
      """Sort the given list using merge sort algorithm and return the sorted list."""
      if len(arr) <= 1:
          return arr

      mid = len(arr) // 2
      left_half = arr[:mid]
      right_half = arr[mid:]

      left_half = merge_sort(left_half)
      right_half = merge_sort(right_half)

      return merge(left_half, right_half)


  def merge(left, right):
      """Merge two sorted lists into a single sorted list and return it."""
      merged = []
      left_index = 0
      right_index = 0

      while left_index < len(left) and right_index < len(right):
          if left[left_index] <= right[right_index]:
              merged.append(left[left_index])
              left_index += 1
          else:
              merged.append(right[right_index])
              right_index += 1

      # Add any remaining elements from the left or right list
      merged.extend(left[left_index:])
      merged.extend(right[right_index:])

      return merged
   '''

Quadratic = n^2
  - Bubble sort
  
    '''
    def bubble_sort(arr):
      """Sort the given list using bubble sort algorithm and return the sorted list."""
      n = len(arr)
      for i in range(n):
          # Last i elements are already sorted
          for j in range(0, n-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
      return arr
  '''
  
Cubic 
  - Matrix multiplication with nested loops
  
    '''
    def matrix_multiply(matrix1, matrix2):
      """Perform matrix multiplication and return the resulting matrix."""
      rows1 = len(matrix1)
      cols1 = len(matrix1[0])
      rows2 = len(matrix2)
      cols2 = len(matrix2[0])

      if cols1 != rows2:
          raise ValueError("Matrix dimensions are incompatible for multiplication.")

      result = [[0] * cols2 for _ in range(rows1)]

      for i in range(rows1):
          for j in range(cols2):
              for k in range(cols1):
                  result[i][j] += matrix1[i][k] * matrix2[k][j]

      return result
  '''

Exponentials
  - Recursive Fibbonacci
  
    '''
    def recursive_fibonacci(n):
      """Compute the n-th Fibonacci number using a recursive algorithm."""
      if n <= 1:
          return n
      else:
          return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
  '''

Big O notation
Big Omega
Big Theta

Justification Techniques
  - By Example
  - Contra Attack
  - Induction and Loop Invariants
  


