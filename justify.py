print("Welcome To Justify")

def right_justify(text):

    l = ""
    count = 71-len(text)
    for i in range(count):

        l = l + " "
    right_justify_text = l + text
    print(right_justify_text)
    # print(len(right_justify_text))
    # print(str(right_justify_text).index("y"))
text = input('Enter text :')
right_justify(text)

