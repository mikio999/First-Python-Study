# [Question-9 (3 points)] 가변인자를 사용하는 함수 average()를 구현하십시오. 이 함수의 인자의 개수는 가변적입니다. 또, 이 함수는 인자의 개수와 그 인자들의 평균값을 함께 반환합니다
def average(*values):
    output = 0
    for value in values:
        output += value
    return len(values), output/len(values)
      
print(average(-3.5, 6.5, 2, 3.3, 5.7))
print(average(-3.3, 3, 2.3, 4))