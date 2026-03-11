print("Welcome to reverse sentence program".title())
word_list = open("C:/Users/user/Documents/word_list.txt").read()

def reverse_sentence(sentence):

    return " ".join(reversed(sentence.split())).capitalize()

sentence = word_list
# sentence = "Reverse this sentence"

print(reverse_sentence(sentence))


