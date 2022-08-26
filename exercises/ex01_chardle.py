"""EX01 - Chardle - A cute step toward wordle."""

_author_ = 730619385

word: str = input("Enter a 5-character word: ")

if len(word) == 5:
    pass
else:
    print("ERROR: Word must contain 5 characters")
    exit()

char_in_word: str = input("Enter a single character: ")

if len(char_in_word) == 1:
    pass
else:
    print("ERROR: Character must be a single character")
    exit()

print("Searching for " + char_in_word + " in " + word)

if char_in_word in word:
    char_location = 0
else:
    print("No instances of " + char_in_word + " found in " + word)
    exit()
if word[char_location] == char_in_word:
    print(char_in_word + " found at index " + str(char_location))
    char_location += 1
else:
    char_location += 1
if word[char_location] == char_in_word:
    print(char_in_word + " found at index " + str(char_location))
    char_location += 1
else:
    char_location += 1
if word[char_location] == char_in_word:
    print(char_in_word + " found at index " + str(char_location))
    char_location += 1
else:
    char_location += 1
if word[char_location] == char_in_word:
    print(char_in_word + " found at index " + str(char_location))
    char_location += 1
else:
    char_location += 1
if word[char_location] == char_in_word:
    print(char_in_word + " found at index " + str(char_location))
print(str(word.count(char_in_word)) + " instances of " + char_in_word)