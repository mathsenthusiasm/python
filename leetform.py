# Leet-speak Translator Program

# Take input from user
sentence = input("Enter any sentence: ")

# Convert to lowercase (so mapping works for all letters)
sentence = sentence.lower()

# Replace letters with leet equivalents
sentence = sentence.replace("a", "4")
sentence = sentence.replace("b", "8")
sentence = sentence.replace("e", "3")
sentence = sentence.replace("i", "1")
sentence = sentence.replace("o", "0")
sentence = sentence.replace("s", "5")
sentence = sentence.replace("t", "7")

# Print result
print("Leet-speak sentence:", sentence)