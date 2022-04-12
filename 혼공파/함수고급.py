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