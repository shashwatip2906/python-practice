import math


def find_gcd_lcm(a, b):
  # Calculate GCD using math.gcd
  gcd_val = math.gcd(a, b)

  # Calculate LCM using the formula: (a * b) // GCD
  lcm_val = abs(a * b) // gcd_val

  return gcd_val, lcm_val


# Test the program:
num1, num2 = 12, 15
g, l = find_gcd_lcm(num1, num2)

print(f"Numbers: {num1} and {num2}")
print(f"GCD: {g}")
print(f"LCM: {l}")

# Output:
# GCD: 3
# LCM: 60