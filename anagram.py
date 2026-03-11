print("Welcome to anagram program".title())

word_list = open("C:/Users/user/Documents/word_list.txt").read().split()
#word_list = ["stop", "musa", "mommy", "fridge", "toyota", "computer", "zebra"]

def is_anagram(check, word_lists):
# check = "zebra"

    for line in word_lists:
        word = line

        if ''.join(sorted(check)) == ''.join(sorted(word)):
            print(word)
            return print(True)
            #print("True\nMatch found", str(check))
        # else:
        #     print(word)
        #     return print(False)
        

# print(check,word)
# print(word_list)
word = "en,do"
print(''.join(sorted(word)))
is_anagram(word, word_list)
