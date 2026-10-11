def is_armstrong(n):
  # Convert the number to a string so we can easily count and loop through its digits
  num_str = str(n)
  num_digits = len(num_str)

  # Calculate the sum of each digit raised to the power of the total digits
  total_sum = 0
  for digit in num_str:
    total_sum += int(digit) ** num_digits

  # If the sum equals the original number, it's an Armstrong number
  return total_sum == n


# Test the program:
print(is_armstrong(153))  # Output: True (1^3 + 5^3 + 3^3 = 153)
print(is_armstrong(120))  # Output: False (1^3 + 2^3 + 0^3 = 9)