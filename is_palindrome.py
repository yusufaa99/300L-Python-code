print("Welcome to palindrome program".title())

word_list = open("C:/Users/user/Documents/word_list.txt").read().split()
# word_list = ["stop", "musa", "mommy", "fridge", "toyota", "computer", "zebra", "noon", "rotator", "madam"]
def reverse_word(word):
    return ''.join(reversed(word))

def is_palindrome(word):
    if len(word) >= 3 and word == reverse_word(word):
        return  True
    else:
        return  False

# word = "rotator"
# is_palindrome(word)

counter = 0
for word in word_list:
    if len(word) >= 3 and is_palindrome(word):
        # print(word)
        counter = counter + 1

print(counter)