# 111
import requests
a = str(input(">> "))
if a.islower() == True:
    print(a.upper())
else:
    print(a.lower())

# 112
score = int(input(">> score: "))
if 80 < score:
    print("grade is A")
elif 60 < score:
    print("grade is B")
elif 40 < score:
    print("grade is C")
elif 20 < score:
    print("grade is D")
else:
    print("grade is E")

# 113
# 보류

money = input(">> 입력(ex. 100 달러) : ").split(' ')
num = money[0]
won = money[1]

if won == "달러":
    print("{} 원".format(float(num) * 1167))
elif won == "엔":
    print("{} 원".format(float(num) * 1.096))
elif won == "유로":
    print("{} 원".format(float(num) * 1268))
elif won == "위안":
    print("{} 원".format(float(num) * 171))


# 114
num1 = int(input(">> input number1 : "))
num2 = int(input(">> input number2 : "))
num3 = int(input(">> input number3 : "))
print(max(num1, num2, num3))

# 115
phone = str(input(">> 휴대전화 번호 입력: "))
p_n = phone.split('-')
if p_n[0] == '011':
    print("당신은 skt 사용자입니다.")
elif p_n[0] == '016':
    print("당신은 kt 사용자 입니다.")
elif p_n[0] == '019':
    print("당신은 lgu 사용자 입니다.")
else:
    print("알수없음.")

# 116
post = str(input(">> 우편번호: "))
if post[2] == '0':
    print("강북구")
elif post[2] == '1':
    print("강북구")
elif post[2] == '2':
    print("강북구")
elif post[2] == '3':
    print("도봉구")
elif post[2] == '4':
    print("도봉구")
elif post[2] == '5':
    print("도봉구")
elif post[2] == '6':
    print("노원구")
elif post[2] == '7':
    print("노원구")
elif post[2] == '8':
    print("노원구")
elif post[2] == '9':
    print("노원구")
else:
    pass

'''
if post[2] in "012":
    print("강북구")
elif post[2] in "345":
    print("도봉구")
elif psot[2] in "6789":
    print("노원구")
'''

# 117
n = input(">> 주민등록번호: ")
n2 = n.split('-')
print(n2)
if n2[1][0] in '13':
    print("남자")
elif n2[1][0] in '24':
    print("여자")
else:
    pass

# 118
n = input(">> 주민등록번호: ")
n2 = n.split('-')
print(n2)
if n2[1][1:3] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
    print("서울 입니다.")
elif n2[1][1:3] in ['09', '10', '11', '12']:
    print("서울이 아닙니다.")
else:
    pass

# 119
n = input(">> 주민등록번호(13자리): ")
if len(n) <= 14:
    n2 = n.split('-')
    a = 2
    total = 0
    for i in range(2):
        # i = 0,1
        for j in range(6):
            if i == 1 & j == 6:
                break
            else:
                ssum = int(n2[i][j]) * a
                #print("{}*{}={}".format(int(n2[i][j]), a, ssum))
                total += ssum

                if a == 9:
                    a = 2
                else:
                    a += 1
    # print(total)
    #print(total % 11)
    if 11-(total % 11) == int(n2[1][-1]):
        print("유효한 주민등록 번호입니다.")
    else:
        print("유효하지 않은 주민등록 번호입니다.")

# 120
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

print("{}:{}".format(key, btc[key]))
# ?? 모듈이 없다는건 뭐지
