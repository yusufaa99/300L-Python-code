print("Welcome to anagram program".title())

word_list = open("wordlist.txt").read().split()
#word_list = ["stop", "musa", "mommy", "fridge", "toyota", "computer", "zebra"]

def is_anagram(check, word_lists):
    found = {}
    check = ''.join(sorted(check))
    for word in word_lists:
        
        if  check == ''.join(sorted(word)):
            if check not in found:
                found[check] = [word]
            else:
                found[check].append(word)
    return found

# def is_anagram(check, word_lists):
#     found = {}
#     check_sorted = ''.join(sorted(check))

#     for word in word_lists:
#         if check_sorted == ''.join(sorted(word)):
#             if check_sorted not in found:
#                 found[check_sorted] = [word]
#             else:
#                 found[check_sorted].append(word)

#     return list(found.values())

def value_count(text):
    value_dic = {}
    for txt in text:
        if txt not in value_dic:
            value_dic[txt] = 1
        else:
            value_dic[txt] += 1
    return value_dic

# print(check,word)
# print(word_list)
word = "tedlas"
word_list2 = ["stop", "musa", "mommy", "fridge", "toyota", "computer", "zebra", 'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled','retainers', 'ternaries', 'generating', 'greatening', 'resmelts', 'smelters', 'termless']
print(word_list2.index('fridge'))

print(is_anagram(word, word_list2))
# print(value_count(word))
# print(word_list)