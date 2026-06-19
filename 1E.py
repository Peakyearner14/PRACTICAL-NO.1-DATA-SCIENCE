sentence = input("Enter a sentence: ")

# Count words and characters
word_count = len(sentence.split())
char_count = len(sentence)

print("Number of words:", word_count)
print("Number of characters:", char_count)

# Lowercase and Uppercase
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())

# Replace spaces with underscores
print("Modified sentence:", sentence.replace(" ", "_"))
