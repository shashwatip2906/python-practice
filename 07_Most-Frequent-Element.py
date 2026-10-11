def most_frequent(lst):
  # Find the item with the highest count using the max() function
  return max(set(lst), key=lst.count)


# Test the program:
numbers = [1, 2, 3, 2, 2, 4, 5, 2]
print(most_frequent(numbers))  # Output: 2