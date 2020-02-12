# 조합
# factorial 함수가 있음 ^^


def fact(num):
    i = 1
    초기값 = num
    while 초기값-1 != i:  # 초깃값==i일때 나온다
        num *= 초기값-i
        # print(num)
        # print(i)
        i += 1
        # print(i)
    return num  # 함수는 return값이 있어야한다(입력값이 있는경우)

# print(fact(5))


수받음 = input("")
b = 수받음.split(" ")
n = int(b[0])
m = int(b[1])
if (5 <= n <= 100) & (5 <= m <= 100) & (m <= n):
    print(fact(n)//(fact(m)*fact(n-m)))
    # 곱셈과 나누기는 묶어서
    # // : 몫이 정수형으로 나옴 /: 몫이 실수형으로 나옴
else:
    print("실패")
