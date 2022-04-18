#set
print(set([2,1,3]))
print(set("Hello World"))
print()

fruits = {'Apple', 'Banana', 'Pineapple'}
mySet = {1.0, 2.0, "Hello World", (1,2,3)} #set 내에 튜플은 ok
print()

math_ = {1,9,7,4,3}
print(sorted(math_))
print(math_)

numbers = set([1,2,3,1,2,3])
print(numbers)
letters = set("abc")
print(letters)

# 세트의 연산
fruits = {"apple", "banana", "grape"}
size = len(fruits)
fruits = {"apple", "banana", "grape"}
if "apple" in fruits:
    print("집합 안에 apple이 있습니다.")
# 입출력 순서가 다른 경우
fruits = {"apple", "banana", "grape"}
for x in fruits:
    print(x, end = " ")
print()
# 정렬한 출력
fruits = {"apple", "banana", "grape"}
for x in sorted(fruits):
    print(x, end = " ")

# 세트에 요소 추가, 제거하기 1
fruits = {"apple", "banana", "grape"}
fruits.add("kiwi")
fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)
fruits.discard("banana")
print(fruits)
fruits.discard("melon")
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)

# 세트에 요소 추가, 제거하기 2
numbers = {1,2,3}
numbers.add(4)
print(numbers)
mySet = {1.0, 2.0, "Hello World", (1,2,3)}
mySet.remove(1.0)
print(mySet)
mySet.update([7, "banana"])
print(mySet)
mySet.discard("banana")
print(mySet)
mySet.clear()
print(mySet)

# 세트 함축 연산
aList = [1,2,3,4,5,1,2]
result = {x for x in aList if x%2==0}
print(result)

# 부분 집합 연산 <, <=, >, >=
A = {"apple", "banana", "grape"}
B = {"apple", "banana", "grape", "kiwi"}

if A < B:
    print("A는 B의 부분 집합입니다.")
if A.issubset(B):
    print("A는 확실히 B의 부분 집합입니다.")

list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))
list2 = [1,2,3,4,5]
list3 = [3,4,5,6,7]
print(set(list2)&set(list3))

# Lab: 문자열의 공통 문자
# 사용자로부터 2개의 문자열을 받아서 두 문자열의 공통 문자를 출력하는 프로그램을 작성해보자.
first_string = input("첫 번째 문자열:")
second_string = input("두 번째 문자열:")
list1 = list(set(first_string)&set(second_string))

print("\n 공통적인 글자:", end =" ")
for i in list1:
   print(i, end= " ")

# Lab:  중복되지 않은 단어의 개수 세기
# 중복되지 않은 단어의 개수 세기
sentence = input("입력 테스트:")
set_list = set(sentence.split())
print("사용된 단어의 개수=",len(set_list))
print(set_list)

# Lab: 파티 동시 참석자 알아내기
# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다.
# 2개 파티에 모두 참석한 사람들의 명단을 출력하려면 어떻게 해야 할까?
partyA = set(["Park","Kim","Lee"])
partyB = set(["Park", "Choi"])
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA&partyB)