# 캐스트 (cast) : 입력받은 문자열을 숫자로 변환
string_a = input("입력A>")
int_a = int(string_a)

string_b = input("입력B>")
int_b = int(string_b)

print( "문자열 자료 :", string_a + string_b)
print( "숫자 자료 :", int_a + int_b)

#int()함수와 float()함수 활용하기
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

#int()함수와 float()함수 조합하기
input_a = float(input("첫 번째 숫자> "))
input_b = float(input("두 번째 숫자> "))
print("덧셈 결과 :", input_a + input_b)
print("뺄셈 결과 :", input_a - input_b)
print("곱셈 결과 :", input_a * input_b)
print("나눗셈 결과 :", input_a / input_b)