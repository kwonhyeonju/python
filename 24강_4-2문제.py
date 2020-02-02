# 1
# dict_a 값 : {}     / {"name": "구름"}
# dict_a에 적용할 코드:
# dict_a["name"]="구름"     /del dict_a["name"]
dict_a = {"name": "구름"}
print(dict_a)
dict_a.clear()
print(dict_a)
# dict_a의 결과 : {"name": "구름"}       / {}

# 2
pets = [
    {"name": "구름", "age": 5},
    {"name": "초코", "age": 3},
    {"name": "아지", "age": 1},
    {"name": "호랑이", "age": 1},
]

print("#우리 동네 애완 동물들")
for pet in pets:
    # print("{} {}살".format(pet, pets[key]))
    print("{} {}살".format(pet["name"], pet["age"]))

# 실행결과
# 우리 동네 애완 동물들
# 구름 5살
# 초코 3살
# 아지 1살
# 호랑이 1살   ***숫자와 문자열 사이에 빈칸이 없이 출력


# 3
# numbers 내부에 들어있는 숫자가 몇 번 등장하는지를 출력하는 코드를 작성해 보세요
numbers = [1, 3, 3, 4, 5, 3, 7, 9, 4, 6, 6, 4, 3, 5, 4, 4, 8, 8, 6, 6, 0]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

 print(counter)

# 실행결과
    # # {1: 1, 3: 4, ...}

# 4
# 다음과 같은 방버으로 특정 값이 어떤 자료형인지 확인 할 수 있다.
# type("문자열") is str
# type([]) is list
# type({}) is dict

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for item in character[key]:
            print("{} : {}".format(key, item))
    else:
        print("{} : {}".format(key, character[key]))


    # 실행결과
    # name : 기사
    # level : 12
    # sword : 불꽃의 검
    # armor : 풀플레이트
    # skill : 베기
    # skill : 세게 베기
    # skill : 아주 세게 베기
