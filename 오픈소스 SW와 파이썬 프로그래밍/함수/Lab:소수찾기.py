# 여기서는 소수를 판별하는 함수 is_prime()을 작성하여 사용하여 보자.
def is_prime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
        else:
            return True
print(is_prime(71))