
def word_distance(text1, text2):
    counter = 0
    text = zip(text1, text2)
    for i in text:
        if i[0] != i[-1]:
            counter += 1
    return counter

text1 = "hello"
text2 = "world"

print(word_distance(text1, text2))


# for i in sorted(text):
#     print(i)
#     if i[0] != i[-1]:
#         counter += 1

# print(counter)