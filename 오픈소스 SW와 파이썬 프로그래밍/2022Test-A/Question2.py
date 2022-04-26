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
