# 1. Iterative Approach (using a loop)
def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


# 2. Recursive Approach (function calls itself)
def factorial_recursive(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial_recursive(n - 1)


# Test the programs (e.g., finding the factorial of 5):
number = 5

print("Iterative result:", factorial_iterative(number))  # Output: 120
print("Recursive result:", factorial_recursive(number))  # Output: 120