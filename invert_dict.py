from utils.structshape import structshape
def value_count(text):
    value_dic = {}
    for txt in text:
        if txt not in value_dic:
            value_dic[txt] = 1
        else:
            value_dic[txt] += 1
    return value_dic

def second_element(t):
    return t[1]

text1 = 'muhammad sani yunus is an engineer'
items = value_count(text1).items()
sorted_items = sorted(items, key=second_element)

def invert_dict(d):
    new = {}
    for key, value in d:
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    return new

print(invert_dict(items))

# from structshape import structshape


data = [
    [1,2],
    [3,4],
    [5,6]
]

a = 7
b = 26
print(divmod(a,b))
print(structshape(data))
