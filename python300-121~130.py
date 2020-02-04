# 121
# 4번

# 122
'''
사과
귤
수박
'''
# 123
'''
사과
--
귤
--
수박
--
'''
# 124
'''
사과
귤
수박
--
'''

# 125
menu = ["김밥", "라면", "튀김"]
for 음식 in menu:
    print("오늘의 메뉴: {}".format(음식))

# 126
portfolio = ["sk하이닉스", "삼성전자", "lg전자"]
for 회사 in portfolio:
    print("{} 보유중".format(회사))

# 127
pets = ['dog', 'cat', 'parrot', 'squirrel', 'goldfish']
for 동물 in pets:
    print("{} {}".format(동물, len(동물)))

# 128
prices = [100, 200, 300]
for 가격 in prices:
    print("{}".format(가격 + 10))

# 129
prices = ["129,300", "1,000", "2,300"]
for 가격 in prices:
    가격1 = 가격.split(',')
    print(가격1[0]+가격1[1])

# 130
menu = ["면라", "밥김", "김튀"]
for 음식 in menu:
    print(음식[::-1])
