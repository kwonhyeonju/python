# 131
my_list = ["가", "나", "다", "라"]
for 한글 in my_list[1:]:
    print("{}".format(한글))

# 132
my_list = [1, 2, 3, 4, 5, 6]
for 숫자 in my_list[::2]:
    print("{}".format(숫자))

# 133
for 숫자 in my_list[1::2]:
    print("{}".format(숫자))

# 134
my_list = ["가", "나", "다", "라"]
for 한글 in my_list[::-1]:
    print("{}".format(한글))

# 135
my_list = [3, -20, -3, 44]
for 숫자 in my_list:
    if 숫자 < 0:
        print(숫자)
    else:
        pass

# 136
my_list = [3, 100, 23, 44]
for 숫자 in my_list:
    if 숫자 % 3 == 0:
        print(숫자)
    else:
        pass

# 137
my_list = ["I", "study", "python", "language", "!"]
for 세문자 in my_list:
    if len(세문자) > 3:
        print(세문자)
    else:
        pass

# 138
my_list = [3, 1, 7, 10, 5, 6]
for 수 in my_list:
    if 5 < 수 < 10:
        print(수)
    else:
        pass

# 139
my_list = [13, 21, 12, 14, 30, 18]
for 수 in my_list:
    if (10 < 수 < 20) & (수 % 3 == 0):
        print(수)
    else:
        pass

# 140
my_list = [3, 1, 7, 12, 5, 16]
for 수 in my_list:
    if (수 % 3 == 0) or (수 % 4 == 0):
        print(수)
