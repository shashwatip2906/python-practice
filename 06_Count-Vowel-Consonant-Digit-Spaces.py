def count_characters(text):
  vowels = "aeiouAEIOU"
  v_count = c_count = d_count = s_count = 0

  for char in text:
    if char in vowels:
      v_count += 1
    elif char.isalpha():  # If it's a letter and not a vowel, it's a consonant
      c_count += 1
    elif char.isdigit():
      d_count += 1
    elif char.isspace():
      s_count += 1

  return v_count, c_count, d_count, s_count


# Test the program:
sentence = "Hello World! 123"
v, c, d, s = count_characters(sentence)

print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Spaces: {s}")

# Output:
# Vowels: 3
# Consonants: 7
# Digits: 3
# Spaces: 2