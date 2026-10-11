def find_pairs_with_sum(numbers, target):
  seen = set()
  pairs = set()

  for num in numbers:
    complement = target - num
    # If the complement exists in our seen set, we found a pair!
    if complement in seen:
      # Sort the pair so we don't return duplicate reverse pairs (like [2,3] and [3,2])
      pair = tuple(sorted((num, complement)))
      pairs.add(pair)
    seen.add(num)

  return list(pairs)


# Test the program:
nums = [2, 4, 3, 5, 7, 8, -1]
target_sum = 7
print(find_pairs_with_sum(nums, target_sum))

# Output: [(2, 5), (3, 4), (-1, 8)] (order may vary)