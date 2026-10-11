def count_words(paragraph):
  # Convert the paragraph to lowercase and split it into a list of words
  words = paragraph.lower().split()

  frequency = {}
  for word in words:
    # Remove basic punctuation attached to words (like commas or periods)
    word = word.strip(".,!?")

    # Count the word using a dictionary
    frequency[word] = frequency.get(word, 0) + 1

  return frequency


# Test the program:
text = "Hello world, hello everyone! Welcome to the world."
result = count_words(text)

for word, count in result.items():
  print(f"'{word}': {count}")

# Output:
# 'hello': 2
# 'world': 2
# 'everyone': 1
# 'welcome': 1
# 'to': 1
# 'the': 1