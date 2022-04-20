# try, except, else, finally
#try except 구문으로 예외를 처리합니다.
try:
    number_input_a = int(input("정수 입력>"))
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14*number_input_a*number_input_a)
except:
    print("정수를 입력해달라고 했잖아요?")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")
    # 파일이 제대로 닫혔는지 확인하기
# try except 구문을 사용합니다.
try:
    file = open("info.txt", "w")
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# try except 구문 끝난 후 파일 닫기
try:
    file = open("info.txt", "w")
    예외.발생해라()
    file.close()
except Exception as e:
    print(e)
# 파일을 닫습니다.
file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")
test()

# finally 키워드 활용
def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except Exception as e:
        print(e)
    finally:
        file.close()
write_text_file("test.txt", "안녕하세요!")

# 반복문과 함께 사용하는 경우
print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")