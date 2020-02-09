# 101
print(input(">> ")*2)

# 102
print(int(input(">> 숫자를 입려가세요: "))+10)

# 103
a = int(input(">> "))
if a % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 104
b = int(input(">> 입력값(0~255): "))
if b+20 < 255:
    print(b+20)
else:
    print("255")

# 105
c = int(input(">> 입력값(0~255): "))
if c-20 < 0:
    print("0")
else:
    print(c-20)

# 106
# ????
#input(">> 현재시간: ")
a = input("현재시간: ")
if a[3:] == "00":
    print("정각입니다.")
else:
    print("정각이 아닙니다.")


# 107
fruit = ["사과", "포도", "홍시"]
d = str(input(">> 좋아하는 과일은? "))
if d in fruit:
    print("정답입니다")
else:
    print("오답입니다.")

# 108
warn_investment_list = ["icrosoft", "google",
                        "naver", "kakao", "samsung", "lg"]
e = str(input(">>투자 경고 종목 리스트: "))
if e in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

# 109
fruit2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
f = str(input(">> 제가 좋아하는 계절은: "))
if f in fruit2:
    print("정답입니다")
else:
    print("오답입니다")

# 110
# 키값은 어떻게 해야하는가?
# ==>>>> values()
fruit2 = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
f = str(input(">> 제가 좋아하는 과일은: "))
if f in fruit2.values():
    print("정답입니다")
else:
    print("오답입니다")
