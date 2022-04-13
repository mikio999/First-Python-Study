# 랜덤하게 1000명의 키와 몸무게 만들기
# 랜덤한 숫자를 만들기 위해 가져옵니다.
import random
# 간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")
# 파일을 쓰기 모드로 엽니다.
with open ("info.txt", "w") as file:
    for i in range(1000):
        # 랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140,200)
        # 텍스트를 씁니다.
        file.write("{}, {}, {}\n" .format(name, weight, height))

with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")
    if (not name) or (not weight) or (not height):
        pass
    bmi = int(weight) / ((int(height)/100)**2)
    result = ""
    if 25 <= bmi:
        result = "과체중"
    elif 18.5 <= bmi:
        result = "정상 체중"
    else:
        result = "저체중"
    print('\n'.join([
        "이름: {}",
        "몸무게: {}",
        "키: {}",
        "BMI: {}",
        "결과: {}"
    ]).format(name, weight, height, bmi, result))
    print()