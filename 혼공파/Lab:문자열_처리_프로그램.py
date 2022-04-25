# 강아지들의 이름을 저장하였다가 출력하는 프로그램을 작성해보자
dog_names = []
while True:
    name = input('강아지의 이름을 입력하시오(종료 시에는 엔터키)')
    if name =="":
        break
    dog_names.append(name)

print('강아지들의 이름:')
for name in dog_names:
    print(name, end=",")