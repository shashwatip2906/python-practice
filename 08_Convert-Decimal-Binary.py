def decimal_to_binary(n):
  # Handle the special case for 0
  if n == 0:
    return "0"

  binary_str = ""

  # Keep dividing by 2 until the number becomes 0
  while n > 0:
    remainder = n % 2  # Get the remainder (0 or 1)
    binary_str = str(remainder) + binary_str  # Add it to the front
    n = n // 2  # Divide the number by 2

  return binary_str


# Test the program:
print(decimal_to_binary(10))  # Output: 1010
print(decimal_to_binary(6))  # Output: 110