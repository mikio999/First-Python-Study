#[Question-5] 당신의 로봇 생산 공장에서 6대의 로봇을 생산하였다. 당신은 그 로봇들 각각에 일련번호와
# 이름을 부여하기를 원한다. 일련번호는 100, 101, 102, ... 과 같이 100부터 시작하여 1씩 증가한 숫자를
# 부여한다. 일련번호가 홀수이면 여성 이름들 중에서, 짝수이면 남성 이름들 중에서 랜덤하게 선택하여, 그
# 로봇에게 이름을 부여한다. 여성 이름들과 남자 이름들의 후보들은 다음과 같이 리스트로 각각 주어져
# 있다. 단, 로봇이름은 중복됨이 없이 서로 다르게 부여한다.

female_names = ["Alice", "Bianca", "Cindy", "Dorothy", "Emily", "Hera", "Isabel", "Jane","Julia", "Lisa", "Monica"]
male_names = ["Alex", "Bradley", "Charles", "Eric", "George", "Harry", "Ivan", "James", "Kevin", "Lucas", "Mickey", "Sam"]

key1 =[]
for i in range(100,106,2):
    key1.append(i)
print(key1)

key2 = []
for i in range(101,107,2):
    key2.append(i)
print(key2)

import random
f_list = random.sample(female_names,3)
m_list = random.sample(male_names, 3)
print(f_list)
print(m_list)

f_name = dict(zip(f_list, key1))
m_name = dict(zip(m_list, key2))

print(f_name)
print(m_name)

f_name.update(m_name)
print(f_name)
final_name = sorted(f_name.items())
print(final_name)

for name in final_name:
    print(name)

# 함수식
import random

def assignName(sn):
    female_name = ['Alice', 'Bianca', 'Cindy', 'Dorothy','Emily', 'Hera', 'Isabel', 'Jane', 'Julia', 'Lisa', 'Monica']
    male_name = ['Alex', 'Bradley', 'Charles', 'Eric', 'George', 'Harry', 'Ivan', 'James', 'Kevin', 'Lucas', 'Mickey', 'Sam']
    
    female_name_length = len(female_name)
    male_name_length = len(male_name)
    if sn%2:
        return female_name[int(sn*random.random()) % female_name_length]
        
    else:
        return male_name[int(sn*random.random()) % male_name_length]
        
name_chosen = []

names={}
#random_serial_list = random.sample(range(100,200),6)
random_serial_list = [100,101,102,103,104,105]

for random_number in random_serial_list:
    name_to_be_assigned = assignName(random_number)
    while (name_to_be_assigned in name_chosen):
        name_to_be_assigned = assignName(random_number)
    
    names[random_number]=name_to_be_assigned
    

print(sorted(names.items()))
reverse_dic = {value : key for key,value in names.items()}
print(sorted(reverse_dic.items()))