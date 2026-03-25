
words_list1 = open("wordlist.txt").read().split()
words_list2 = ["listen","silent","enlist","evil","vile","veil","live","cat","act","man", "dam"]

# nomal version of the solution
def group_anagram(word_lists):
    anagrams = {}
    newanagram = {}
    key = ''
    for word in word_lists:
        key = ''.join(sorted(word))
        if  key == ''.join(sorted(word)):
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
                
    # this is implemented because i wand to see a list of anagram with more than one items
    for i,j in anagrams.items():
        if len(anagrams[i]) != 1:
            # using if-else block which gives me what i am expecting.
            if i not in newanagram:
                newanagram[i] = j
            else:
                newanagram[i].append(j)

            # using setdefauld method but it creating addition list to the required list
            # newanagram.setdefault(i, []).append(j)
    return newanagram

# improve version of the solution using inbuild method "setdefault"
def group_anagram2(word_lists):
    anagrams = {}
    
    for word in word_lists:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)

    return anagrams

print(group_anagram(words_list1))