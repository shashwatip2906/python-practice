def is_palindrome(n):
  # Convert the number to a string and check if it equals its reverse
  num_str = str(n)
  return num_str == num_str[::-1]


# Test the program:
print(is_palindrome(121))  # Output: True
print(is_palindrome(123))  # Output: False