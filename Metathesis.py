# def word_distance(text1, text2):
#     counter = 0
#     text = zip(text1, text2)
#     for i in text:
#         if i[0] != i[-1]:
#             counter += 1
#     return counter

# text1 = "hello"
# text2 = "world"

# print(word_distance(text1, text2))

check = 'form'
word_lists = open("wordlist.txt").read().split()
sorted_check = ''.join(sorted(check))

anagrams = {}
    
for word in word_lists:
    key = ''.join(sorted(word))
    anagrams.setdefault(key, []).append(word)

# print(anagrams)
for word in word_lists:
    counter = 0
    if  sorted_check == ''.join(sorted(word)):  
        text = zip(check, word )
        for i in text:
            if i[0] != i[-1]:
                counter += 1
        if counter == 2:
            print(check, word)
    