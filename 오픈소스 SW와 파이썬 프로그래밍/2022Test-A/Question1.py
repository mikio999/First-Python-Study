contacts = {"Kim":"010-111-1234","Park":"010-222-2345","Lee":"010-333-3456"}
while True:
    name = input("Enter friend's name: ")
    if name == '':
        break
    else:
        print(contacts.get(name))
        
# 함수식
def sort_and_print(text):
    dict ={}
    for num in text:
        if num in dict:
            dict[num]+=1
        else:
            dict[num]=1
    for key, value in sorted(dict.items()):
        print("'"+str(key)+"' : '"+str(value)+"'")
    print(sorted(list(map(int, set(text.split(','))))))

input_text = input("Enter a line of integers:")
while(input_text != ""):
	sort_and_print(input_text)
	input_text = input("Enter a line of integers:")
