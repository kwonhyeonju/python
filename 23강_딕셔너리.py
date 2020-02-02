# 딕셔너리 선언
딕셔너리 = {
    "문자열": "값",
    273: [1, 2, 3, 4],
    True: False
}

# 반복문
for key in 딕셔너리:
    print("키값 : ", key)
    print("-> {} : {}".format(key, 딕셔너리[key]))

# 요소 추가
딕셔너리["요소추가"] = "값"
print()  # \n
for key in 딕셔너리:
    print("키값 : ", key)
    print("-> {} : {}".format(key, 딕셔너리[key]))

# 요소 제거
del 딕셔너리["요소추가"]
print()
for key in 딕셔너리:
    print("키값 : ", key)
    print("-> {} : {}".format(key, 딕셔너리[key]))
