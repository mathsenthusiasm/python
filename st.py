from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    
    for word in strs:
        key = ''.join(sorted(word))   # sorted letters used as key
        anagram_map[key].append(word)
    
    return list(anagram_map.values())


# ---- Main Program ----
n = int(input("Enter number of words: "))   # number of strings
strs = []#empty list

for i in range(n):
    word = input(f"Enter word {i+1}: ")
    strs.append(word)

print("Grouped Anagrams:")
print(groupAnagrams(strs))