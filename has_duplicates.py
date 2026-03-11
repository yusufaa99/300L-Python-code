# a program that checks for duplicate element in the squence of string
# it return true if the element is found in the string more than onece
# it return false if the element is found in the string onece
def has_duplicates(text):
    for txt in text:
        if text.count(txt) > 1:
            return True
        else:
            return False

text = "musam"      
print(has_duplicates(text))
