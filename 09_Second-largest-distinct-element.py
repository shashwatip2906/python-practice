def second_largest(numbers):
  # Remove duplicates with a set, then sort the numbers
  unique_nums = sorted(list(set(numbers)))

  # Check if there are at least two distinct numbers
  if len(unique_nums) < 2:
    return "Not enough distinct elements"

  # The second to last element is our second largest
  return unique_nums[-2]


# Test the program:
my_list = [10, 20, 4, 45, 99, 99]
print(second_largest(my_list))  # Output: 45