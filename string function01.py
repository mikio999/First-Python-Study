# format() 함수로 숫자를 문자열로 변환하기
string_a = "{}" .format(10)

# 출력하기
print(string_a)
print(type(string_a))

# format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만 원" .format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기" .format(5000)
format_c = "{} {} {}" .format(3000, 4000, 5000)
format_d = "{} {} {}" .format(1, "문자열", True)

# 출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)

print(type(format_a))
print(type(format_b))
print(type(format_c))
print(type(format_d))

# 정수
output_a = "{:d}" .format(52)

# 특정 칸에 출력하기
output_b = "{:5d}" .format(52)
output_c = "{:10d}" .format(52)

# 빈칸을 0으로 채우기
output_d = "{:05d}" .format(52)
output_e = "{:05d}" .format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력하기")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)