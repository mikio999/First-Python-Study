# [Question-6 (5 points)] 당신은 친구들의 전화번호들을 다음과 같이 딕셔너리 자료형으로 관리하고 있다고
# 가정합시다. Suppose you are managing your friends' phone numbers in dictionary data type as follows:
# contacts = {'Kim':'01012345678', 'Park':'01012345679', 'Lee':'01012345680'}
# 사용자로 부터 이름을 입력받고, 그 이름이 contacts에 있으면, 그 전화번호를 출력하고 (이 경우에는
# 출력형식은 임의입니다), 그 이름이 contacts에 없으면, "None"을 출력합니다. 이 것을 무한히
# 반복합니다. 단, 사용자가 이름을 입력하지 않고 Enter key를 누르면, 그 프로그램을 종료합니다. 

contacts =  {'Kim':'01012345678', 'Park':'01012345679', 'Lee':'01012345680'}

while True:
    name = input('name:')
    if name == '':
        break
    else:
        print(contacts.get(name))