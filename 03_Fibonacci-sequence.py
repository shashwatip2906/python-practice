def generate_fibonacci(n):
  # Start with the first two numbers of the series
  fib_series = [0, 1]

  # Generate the rest of the numbers up to n terms
  for i in range(2, n):
    next_number = fib_series[-1] + fib_series[-2]
    fib_series.append(next_number)

  return fib_series[:n]


# Test the program (e.g., generate 10 terms):
print(generate_fibonacci(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]