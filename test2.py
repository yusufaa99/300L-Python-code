words_list = open("wordlist.txt").read().replace('-', ' ').strip().split()
words_list2 = ['superiors-behold!','chocolate-coloured','coolness-frightened','gentleman-something',"listen","silent","enlist","evil","vile","veil","live","cat","act","man", "dam"]
word = ['spite', 'spit', 'pit', 'it', 'i']
text = 'Sprite'
unique = {}

for i in words_list2:
    unique[i] = 1

print(len(unique))

print(sorted(unique, key = len)[-5:])

unique_words = {}
for line in words_list2:
    seq = line.replace('-', ' ').strip().split()
    for word in seq:
        unique_words[word] = 1

print(len(unique_words))
print(sorted(unique_words, key = len)[-5:])



# debug the following code, its not working as expected
reg_no = ['u24co2023', 'u23cv1098', 'u23me2021', 'u25co1001', 'u23mc1021', 'u21ee1011', 'u20ee1027', 'u21co2017']
reg_no_co = []
reg = ['co', 'cv', 'ee', 'me', 'mc', 'am', 'cm']
order_reg_no = []

reg_no_dic = {}

#  a simple program that filter reg numbers which belong to co and which does not.
for reg in reg_no:
    if 'co' not in reg:
        order_reg_no.append(reg)
    else:
        reg_no_co.append(reg)

# print('CO', reg_no_co)
# print('NON CO', order_reg_no)
