from collections import Counter


def list_intersection(list1, list2):
  # Count the frequency of each element in both lists, then find their intersection
  return list((Counter(list1) & Counter(list2)).elements())


# Test the program:
a = [1, 2, 2, 1, 3]
b = [2, 2, 3, 3]
print(list_intersection(a, b))

# Output: [2, 2, 3]