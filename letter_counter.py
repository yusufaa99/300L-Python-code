
def letter_counter(text):

    counter = {}
    for letter in text:

        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return  counter


text = "muhammad sani yunusa"
print(letter_counter(text))

for key in letter_counter(text):
    print(key)

for values in letter_counter(text).values():
    print(values)

# access the key and value at the same time through the loop, "but not working as expected
# for key in letter_counter(text):
#     values = letter_counter(key).values()
#     print(key, values)