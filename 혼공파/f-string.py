# 1. f-string 기본 사용법
names = ['민경','민준','민돌','민순']
nums = [24, 29, 21, 19]
for name, age in zip(names, nums):
    print(f'{name}의 나이는 {age}이다.')

for x in range (1,10):
    print(f'{x} x 2 = {x*2}입니다.')

# 2. 글자 수를 지정하여 문자열을 정렬
names = ['민경','민준','민돌','민순']
nums = [24, 29, 21, 19]
for name, age in zip(names, nums):
    print(f'{name:10s}의 나이는 {age:^10d}이다.')

for x in range (1,10):
    print(f'{x:>10d} x 2 = {x*2}입니다.')

# 3. 소수점 자릿수 지정
float = {0.5678,0.6666,1.452343}
for f in float:
    print(f'세번째 자리까지 표현 {f:.3f}')