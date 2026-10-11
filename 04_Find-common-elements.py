def find_common_elements(list1, list2):
  # Convert both lists to sets and find their intersection using '&'
  return list(set(list1) & set(list2))


# Test the program:
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(find_common_elements(a, b))  # Output: [4, 5] (order may vary)