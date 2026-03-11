# Write a function called shift_word that takes as parameters a string and
# an integer, and returns a new string that contains the letters from the string
# shifted by the given number of places.
# To test your function, confirm that “cheer” shifted by 7 is “jolly” and
# “melon” shifted by 16 is “cubed”.

def shift_word(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in text.lower():

        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            result += alphabet[new_index]
        else:
            result += char

    return result

word = shift_word("cheer", 7)
print(word)