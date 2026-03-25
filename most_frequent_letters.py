"Write a function called most_frequent_letters that takes a string and"
"prints the letters in decreasing order of frequency."
def most_frequent_letters(text):
    text = sorted(text, reverse=True)
    return ''.join(text)

text = "cisco"

print(most_frequent_letters(text))