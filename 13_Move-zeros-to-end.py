def move_zeros_to_end(lst):
  # Collect all non-zeros, then add back the correct number of zeros at the end
  return [x for x in lst if x != 0] + [0] * lst.count(0)


# Test the program:
numbers = [0, 1, 9, 0, 4, 12, 0, 6]
print(move_zeros_to_end(numbers))

# Output: [1, 9, 4, 12, 6, 0, 0, 0]