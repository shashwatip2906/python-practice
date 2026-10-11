def longest_substring(s):
  seen = {}
  start = 0
  max_len = 0
  longest = ""

  for end, char in enumerate(s):
    # If the character was seen and is inside our current window
    if char in seen and seen[char] >= start:
      start = seen[char] + 1

    seen[char] = end

    # Check if this new substring is longer than our previous max
    if end - start + 1 > max_len:
      max_len = end - start + 1
      longest = s[start : end + 1]

  return longest


# Test the program:
print(longest_substring("abcabcbb"))  # Output: abc
print(longest_substring("bbbbb"))  # Output: b
print(longest_substring("pwwkew"))  # Output: wke