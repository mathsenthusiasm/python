def groupAnagrams(strs):
    groups = {}#empty dictionary
    for word in strs:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]
    return list(groups.values())

# Take input from the user after program runs
user_input = input("Enter words separated by space: ")

# Convert input string into list of words
words = user_input.split()

# Call the function with the list of words
result = groupAnagrams(words)

# Print the grouped anagrams
print(result)
