# 딕셔너리 dictionary
{
    "키A" : 10,
    "키B" : 20,
    "키C" : 30,
    1:     40,
    False : 50
}

dict_a = {
    "name" : "어밴저스 엔드게임",
    "type" : "히어로 무비"
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])

dict_b = {
    "director": ["안소니 루소", "조 루소"],
    "cast": ["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
}
print(dict_b)
print(dict_b["director"])

# 딕셔너리 요소에 접근하기
dictionary= {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name :",dictionary["name"])
print("type :",dictionary["type"])
print("ingredient :",dictionary["ingredient"])
print("origin :", dictionary["origin"])

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

print(dictionary["ingredient"][1])

dictionary["price"] = 5000
print(dictionary)

dictionary["name"] = "8D 건조 파인애플"
print(dictionary)

del dictionary["type"]
print(dictionary)

# 딕셔너리에 요소 추가하기
dictionary = {}
print("요소 추가 이전:",dictionary)
dictionary["name"] = "새로운 이름"
dictionary['head'] = "새로운 정신"
dictionary['body'] = "새로운 몸"
print("요소 추가 이후:", dictionary)

# 딕셔너리에 요소 제거하기
dictionary = {
    "name" : "7D 망고절임",
    "type" : "당절임"
}
print("요소 제거 이전:", dictionary)
del dictionary["type"]
print("요소 제거 이후:", dictionary)

# 키가 존재하는지 확인하고 값에 접근하기
dictionary= {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

key = input("> 접근하고자 하는 키:")
if key in dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# 키가 존재하지 않을 때 None을 출력하는지 확인하기
dictionary= {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
value = dictionary.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")

# for 반복문과 딕셔너리
dictionary= {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}
for key in dictionary:
    print(key, ":", dictionary[key])

# 확인문제 1번
dict_a ={}
dict_a["name"] = "구름"
print(dict_a)
del dict_a["name"]
print(dict_a)

# 확인문제 2번
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1}
]
print("#우리 동네 애완 동물들")
for pet in pets:
    print(pet["name"],str(pet["age"]), "살")

# 2트
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age":1}
]
print("# 우리 동네 애완 동물들")
for pet in pets:
    print(pet["name"],str(pet["age"])+"살")

numbers = [1,2,6,8,4,3,2,1,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter :
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1
    
    print(counter)
    
# 딕셔너리를 선언합니다.
character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
    }
    

