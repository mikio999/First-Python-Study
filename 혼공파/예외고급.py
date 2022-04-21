# 예외 객체 Exception
try:
    number_input_a = int(input("정수 입력>"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:",3.14*number_input_a*number_input_a)
except Exception as exception:
    print("type(exception):". type(exception))
    print("exception:",exception)

# 여러 가지 예외가 발생할 수 있는 코드
list_number = [52,273,32,72,100]
try:
    number_input = int(input("정수 입력>"))
    print("{}번째 요소:{}".format(number_input, list_number[number_input]))
except Exception as exception:
    print("type(exception):", type(exception))
    print("exception:",exception)
# 예외 구분하기
list_number = [52,273,32,72,100]
try:
    number_input = int(input('정수 입력>'))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해 주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")

# 예외 구문과 예외 객체
list_number = [52,273,32,72,100]
try:
    number_input = int(input('정수 입력>'))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print("exception:", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception:", exception)
    # 모든 예외 잡기
list_number = [52,273,32,72,100]
try:
    number_input = int(input('정수 입력>'))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해 주세요!")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception), exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)
# 아직 구현되지 않은 부분에서 강제로 예외 발생시키기
number = input("정수 입력>")
number = int(number)
if number > 0 :
    raise NotImplementedError
else:
    raise NotImplementedError