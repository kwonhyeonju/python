# 30강 연습문제
# 2 __ 1~100/2진수 / 0이 하나만 포함된 숫자의 합
output = 0

for i in range(1, 101):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i, i))
        output += i
print("합계: ", output)

# 리스트 내포를 이용
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
