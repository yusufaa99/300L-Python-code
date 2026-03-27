
words = [
    # Metathesis pairs
    "form", "from",
    "calm", "clam",
    "spot", "stop",
    "note", "tone",
    "brag", "grab",
    "act", "cat",
    "inch", "chin",

    # Anagram groups (more than 2)
    "listen", "silent", "enlist", "tinsel",
    "evil", "vile", "veil", "live",
    "dusty", "study",
    "night", "thing",

    # Interlocking words
    "shoe", "cold", "schooled",
    "rise", "road", "risoed",

    # Normal words (no pairs)
    "apple", "banana", "orange", "grape",
    "chair", "table", "bread", "water",
    "school", "teacher", "student",

    # Words with small differences
    "stone", "stony",
    "plane", "panel",
    "heart", "earth"
]


word_lists = open("wordlist.txt").read().split()

def metathesis_func(words):
    anagrams = {}
        
    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)

    metathesis = {}
    for key,group in anagrams.items():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    counter = 0
                    word1 = group[i]
                    word2 = group[j]
                    text = zip(word1, word2)
                    for a,b in text:
                        if a != b:
                            counter += 1
                            
                    if counter == 2:
                        metathesis.setdefault(key, []).append((word1, word2))

    for key, pair in metathesis.items():
        print(key, " ", pair)

metathesis_func(words)
    





# the following code is an upgraded version of the code and its upgraded by AI assistant (GPT) in order to understand the solution better
def metathesis_func2(words):
    anagrams = {}

    # Step 1: Group anagrams
    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)

    # Step 2: Find metathesis pairs
    metathesis = {}

    for key, group in anagrams.items():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    word1 = group[i]
                    word2 = group[j]

                    diff = []

                    for index, (a, b) in enumerate(zip(word1, word2)):
                        if a != b:
                            diff.append(index)

                    if len(diff) == 2:
                        i1, i2 = diff
                        if word1[i1] == word2[i2] and word1[i2] == word2[i1]:
                            metathesis.setdefault(key, []).append((word1, word2))

    return metathesis


# Call function
result = metathesis_func2(words)

for key, pairs in result.items():
    print(key, "→", pairs)