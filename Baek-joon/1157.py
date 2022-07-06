word = input().upper()
word_list = list(set(word))

alphabet_list = []
for x in word_list:
    word_count = word.count
    alphabet_list.append(word_count(x))

if alphabet_list.count(max(alphabet_list)) != 1:
    print("?")
else:
    print(word_list[(alphabet_list.index(max(alphabet_list)))])