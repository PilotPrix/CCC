# https://dmoj.ca/problem/ccc15j3

'''
for each consonant:
- consonant itself
- nearest vowel
- next consonant
'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowel = ["a", "e", "i", "o", "u", "y"]
x = input()
# For each consonant
for y in x:
  ## Add consonant to string
  z = y
  
  ## Add nearest vowel
  # Get left and right vowel distance
  j = alphabet.find(y)

  # Backwards
  i = j
  while i > 0:
    if alphabet[i] in vowel:
      break
    i -= 1
  leftDiff = abs(i - j)
  
  # Forwards
  i = j
  while i < 25:
    if alphabet[i] in vowel:
      if i == j:
        j = 0
      break
    i += 1

  if i == j:
    rightDiff = 26
  else:
    rightDiff = abs(i - j)

  # Get shortest difference, use that vowel, if equal, use left vowel
  if leftDiff <= rightDiff:
    print(alphabet[j - leftDiff])
  else:
    print(alphabet[j + rightDiff])

