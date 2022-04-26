contacts = {"Kim":"010-111-1234","Park":"010-222-2345","Lee":"010-333-3456"}
while True:
    name = input("Enter friend's name: ")
    if name == '':
        break
    else:
        print(contacts.get(name))
