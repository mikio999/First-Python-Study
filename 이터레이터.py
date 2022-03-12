# iterable 이터러블 : 반복할 수 있는 것, 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체
# ex) 리스트, 딕셔너리, 문자열 튜플

# reversed 함수와 이터레이터
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)
print("reversed_numbers :", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

output = [i for i in range(1,101)
    if "{:b}".format(i).count("0")==1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("합계:", sum(output))