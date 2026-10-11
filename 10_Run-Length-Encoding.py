def run_length_encoding(text):
  if not text:
    return ""

  encoded = []
  count = 1

  # Loop through the string starting from the second character
  for i in range(1, len(text)):
    if text[i] == text[i - 1]:
      count += 1
    else:
      # Append the previous character and its count
      encoded.append(text[i - 1] + str(count))
      count = 1

  # Don't forget to add the very last character and its count
  encoded.append(text[-1] + str(count))

  return "".join(encoded)


# Test the program:
print(run_length_encoding("aaabbcccc"))  # Output: a3b2c4
print(run_length_encoding("wwwbbbw"))  # Output: w3b3w1