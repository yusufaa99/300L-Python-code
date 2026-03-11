t = tuple('tuples')
a = tuple()
b = tuple()
print(type(a))
d = {}
d[2,5] = 6
d[4,8] = 3
t = d[4,8]
name = ['musa', 'sani', 'garba', 'hadi', 'jafar']
score = (45, 78, 67, 54, 65)
# a,b = 10, 20,
temp = a
a = b
b = temp
email = "example@gmail.com"
username, domain = email.split("@")
provider, domain = domain.split('.')
for i in name:
    i = score
    print(i)
a, *b, c = (1,2,3,4,5.6,7)

def get_student(*args):
    return ("parkage arguments :", args)

students = [("Yusuf", 3.8), ("Ali", 3.5)]
args_text = (1,2,3.5,'thia is packaging')
for name, gpa in students:
    print(name, gpa)

t = (1, 2, 3)

def sum(a,b,c):
    return a+b+c


try:
    t[2] += [4]
except TypeError:
    pass
add = 0
for i in range(3,33, 5):
    print(i)
    add += i
for i in range(33):
    print(i)

dicts = {'one':1, 'two': 2, 'three':3}
for i in dicts.items():
    key, value = i
    print(f"{key}-> {value}")

def quotient_remender(value, div):
    return(f'{value} devide by {div} is :', value//div, 'remender', value%div)

scores1 = [1, 2, 4, 5, 1, 5, 2, 9]
scores2 = [5, 5, 2, 2, 5, 2, 3, 0]

lst = []
for pair in zip(scores1, scores2):
    lst += pair
print(lst)

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
#  using range and zip functions to access the index and values of the dict
for i, j in letter_map.items():
    print(i,j)

#  using enumerate function methods to access the index and values of the dict
print('enumerate')
for i, j in enumerate(letters):
    print(i,j)

print(*quotient_remender(20, 7))

print(divmod(20, 7))
print('sum is :', add)

print(t)
num = range(100)
print(num)
k = 1
while k <= len(num):
    print(k)
    k += 1
a = [1,2,3]
b = [4,5,6]

z = zip(a,b)
it = iter(z)

print(next(z))
for a in z:
    print(a)
print(next(z, "END"))
# print(list(z))
print(username, domain, provider, a, b, c, get_student(args_text, '76, 87', 87), t, sum(*t))

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

val = value_count(text1).values()
keys = value_count(text1).keys()
print(val, keys)

