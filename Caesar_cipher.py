letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
print(letter_map)

# my code for the encryption
# def encrypt(text):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     text = text.lower()
#     k =3
#     e = ''
#     for i in text:
#         p = letters.index(i)
#         c = (p + k)%26
#         e += letters[c]
#     return e

# text = "nesoAcademy"
# encrypted = encrypt(text)
# print(encrypted)

# inproved version of the code by AI assitant (Chat GPT)
def encrypt(text, shift=3):
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

text1 = encrypt("nesoAcademy")
text2 = encrypt("Muhammad sani yunusa")
text3 = encrypt("example@gmail.com")
print(text1)
print(text2)
print(text3)

# code for decrypting
def decrypt(text, shift=3):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    text = text.lower()
    for char in text:

        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % 26
            result += alphabet[new_index]
        else:
            result += char

    return result

text4 = decrypt(text1)
text5 = decrypt(text2)
text6 = decrypt(text3)
print(text4)
print(text5)
print(text6)