def flatten_list(nested_list):
  flat = []
  for item in nested_list:
    # If the item is another list, flatten it recursively
    if isinstance(item, list):
      flat.extend(flatten_list(item))
    else:
      flat.append(item)
  return flat


# Test the program:
nested = [1, [2, [3, 4], 5], [6, 7], 8]
print(flatten_list(nested))

# Output: [1, 2, 3, 4, 5, 6, 7, 8]