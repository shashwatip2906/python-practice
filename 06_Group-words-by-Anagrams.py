def group_anagrams(words):
  anagrams = {}
  for word in words:
    # Sort the letters of the word to use as a unique key
    key = "".join(sorted(word))
    # Group the original word under its sorted key
    anagrams.setdefault(key, []).append(word)

  return list(anagrams.values())


# Test the program:
word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(word_list))

# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]