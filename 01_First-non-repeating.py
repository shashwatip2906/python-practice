def first_non_repeating(text):
  for char in text:
    # If the character appears only once in the string, return it
    if text.count(char) == 1:
      return char
  return None  # Return None if all characters repeat


# Test the program:
print(first_non_repeating("swiss"))  # Output: w
print(first_non_repeating("programming"))  # Output: p
print(first_non_repeating("aabbcc"))  # Output: None