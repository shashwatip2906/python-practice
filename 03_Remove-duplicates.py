def remove_duplicates(my_list):
  # dict.fromkeys() removes duplicates and Python dictionaries preserve insertion order
  return list(dict.fromkeys(my_list))


# Test the program:
numbers = [1, 2, 3, 2, 4, 1, 5]
print(remove_duplicates(numbers))

# Output: [1, 2, 3, 4, 5]