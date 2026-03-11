def is_interlocking(text):
    word = {'shoe', 'cold', 'hight', 'so', 'sum', 'do'}
    even = text[0::2]
    odd = text[1::2]
    if even in word and odd in word:
        return True
    else:
        return False

text = 'schooled'
print(is_interlocking(text))
# print(txt[0::2])
# print(txt[1::2])  