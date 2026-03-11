# conuting the appearance of letters in a given text using if statement to handle tyhe occurances
def value_count(text):
    value_dic = {}
    for txt in text:
        if txt not in value_dic:
            value_dic[txt] = 1
        else:
            value_dic[txt] += 1
    return value_dic



# conuting the appearance of letters in a given text using inbuild dictionary method "get" handle tyhe occurances
# def value_count2(text):
#     value_dic = {}
#     for txt in text:
#         value_dic[txt] = 1 
#         # value_dic2[txt] = value_dic2.get(txt)

#     return value_dic


counter1 = value_count('brontosaurus')
counter2 = value_count('apatosaurus')
print(counter1)
print(counter2)

# test before creating th add_counters function
# for txt in counter1:
#     if txt not in counter2:
#         counter2[txt] = counter1.get(txt)
#     else:
#         counter2[txt] += counter1.get(txt)
# print(counter2)

def add_counters(counter1, counter2):
    for txt in counter1:
        if txt not in counter2:
            counter2[txt] = counter1.get(txt)
        else:
            counter2[txt] += counter1.get(txt)
    return counter2

print(add_counters(counter1, counter2).items())
# text1 = "muhammad sani garba from kaduna polytechnic kaduna, nigeria"
# text2 = "apatosaurus"

# print(counter2)
