def generate_tables(start, end):
  # Loop through each number in the given range
  for i in range(start, end + 1):
    print(f"\n--- Table of {i} ---")
    # Loop from 1 to 10 to generate the multiplication table
    for j in range(1, 11):
      print(f"{i} x {j} = {i * j}")


# Test the program (generate tables for numbers 2 to 3):
generate_tables(2, 3)