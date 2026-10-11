def rotate_list(lst, k):
  if not lst:
    return lst
  # Handle cases where k is larger than the list length
  k = k % len(lst)
  # Slice and rearrange the list
  return lst[-k:] + lst[:-k]


# Test the program (rotate right by 2 positions):
numbers = [1, 2, 3, 4, 5]
print(rotate_list(numbers, 2))  # Output: [4, 5, 1, 2, 3]