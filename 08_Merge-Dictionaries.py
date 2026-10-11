def merge_dictionaries(dict1, dict2):
  # Start with a copy of the first dictionary
  merged = dict1.copy()

  for key, value in dict2.items():
    if key in merged:
      # If the key already exists, handle it (e.g., add their values together)
      merged[key] += value
    else:
      # If it's a new key, just add it normally
      merged[key] = value

  return merged


# Test the program:
d1 = {"apple": 5, "banana": 3}
d2 = {"banana": 2, "cherry": 4}

print(merge_dictionaries(d1, d2))
# Output: {'apple': 5, 'banana': 5, 'cherry': 4}