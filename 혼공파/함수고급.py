tuple_test = (10,20,30)
tuple_test[0] #10
tuple_test[1] #20
tuple_test[2] #30
# 튜플은 내부 요소 변경이 불가능

# 리스트와 튜플의 특이한 사용
[a,b] = [10,20]
(c,d) = (10,20)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 괄호가 없는 튜플
tuple_test = 10, 20, 30, 40
print("# 괄호가 없는 튜플의 값과 자료형 출력")
print("tuple_test :", tuple_test)
print("type(tuple_test):", type(tuple_test))
print()

# 괄호가 없는 튜플 활용
a,b,c = 10, 20, 30
print("# 괄호가 없는 튜플을 활용한 할당")
print("a:", a)
print("b:", b)
print("c:", c)

# 변수의 값을 교환하는 튜플
a, b = 10, 20

print("# 교환 전 값")
print("a:", a)
print("b:", b)
print()

# 값을 교환한다.
a,b = b,a
print("a:", a)
print("b:", b)
print()

# 튜플과 함수
# 여러 개의 값 리턴하기
def test():
    return (10,20)
a,b = test()
print("a:", a)
print("b:", b)

# 튜플을 리턴하는 함수의 예시
for i, value in enumerate([1,2,3,4,5,6]):
    print("{}번째 요소는 {}입니다." .format(i,value))

a,b = 97, 40
print(a//b)
print(a%b)
print(divmod(a,b))

# 람다 Lamda : 함수라는 '기능'을 매개변수로 전달하는 코드를 많이 사용

# 함수의 매개 변수로 함수 전달하기
# 매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()
# 간단한 출력하는 함수
def print_hello():
    print("안녕하세요")
call_10_times(print_hello)

# filter() 함수와 map() 함수
# map(함수, 리스트)
# filter(함수, 리스트)
def power(item):
    return item*item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]

# map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power,list_input_a):", output_a)
print("map(power,list_input_a):", list(output_a))
print()
# filter() 함수를 사용합니다.
output_b = filter(under_3,list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 람다 
power = lambda x : x*x
under_3 = lambda x : x<3

list_input_a = [1,2,3,4,5]

output_a = map(power,list_input_a)
print("map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 변수를 선언합니다.
list_input_a = [1,2,3,4,5]

# map() 함수를 사용합니다.
output_a = map(lambda x: x*x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a):", output_a)
print("map(power, list_input_a):", list(output_a))
print()

output_b = filter(lambda x: x<3, list_input_a)
print("# filter() 함수의 실행결과")
print("filter(under_3, list_input_a):", output_b)
print("filter(under_3, list_input_a):", list(output_b))

# 파일 처리
# 파일 열고 닫기
file = open("basic.txt", "w")
file.write("Hello Python Programming...!")
file.close()

# read() 함수로 텍스트 읽기
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)
