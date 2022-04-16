# [Question-7 (5 points)] 매 반복에서, 사용자로 부터 한개의 문장을 입력 받습니다. 그 문장에는
# 구두점기호(마침표, 콤마, 따옴표 등)는 포함되어 있지 않고, 숫자, 스페이스문자, 알파벳 소문자와 알파벳
# 대문자만 포함합니다. 알파벳 대문자는 소문자로, 알파벳 소문자는 대문자로 바꾸어 출력하되, 알파벳
# 대문자 A와 소문자 a를 출력하지 않습니다. 이 것을 무한히 반복합니다. 사용자로부터 입력받은 문장에
# 숫자 2가 포함되어 있으면, 그 문장은 처리하되, 다음 입력을 받지 않고, 그 프로그램을 종료합니다.

while True:
    sentence = input("Enter a sentence :")
    if sentence.find('2') == -1:
        result = sentence.swapcase()
        print(result.replace('a', '').replace('A',''))
    else:
        result = sentence.swapcase()
        print(result.replace('a', '').replace('A',''))
        break
