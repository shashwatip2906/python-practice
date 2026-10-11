def is_prime(n):
  return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
print(is_prime(11))  # Output: True
print(is_prime(4))  # Output: False