# 두개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자.
def big_number(x,y):
    if (x>y):
        return x
    else:
        return y
print(big_number(4,5))