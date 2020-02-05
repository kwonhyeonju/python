# 141
my_list = ["A", "b", "c", "D"]
for 알파벳 in my_list:
    if 알파벳.isupper():
        print(알파벳)
    else:
        pass

# 142
print("142번")
for 알파벳 in my_list:
    if 알파벳.islower():
        print(알파벳)
    else:
        pass

# 143
# 어떻게 합치지?

for 알파벳 in my_list:
    if 알파벳.islower():
        print(알파벳.upper(), end="")
    else:
        print(알파벳.lower(), end="")
print()



# 144
file_list = ['hello.py', 'ex01.py', 'ch02.py', 'intro.hwp']
for 파일 in file_list:
    파일이름 = 파일.split('.')
    print(파일이름[0])

# 145
filenames = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 파일 in filenames:
    파일이름 = 파일.split('.')
    if 파일이름[1] == 'h':
        print(파일)

# 146
for 파일 in filenames:
    파일이름 = 파일.split('.')
    if (파일이름[1] == 'h') | (파일이름[1] == 'c'):
        print(파일)

# 147
my_list = [3, -20, -3, 44]
new_list = []
for 양수 in my_list:
    if 양수 > 0:
        # print(양수)
        new_list.append(양수)
print(new_list)

# 148
my_list = ["A", "b", "c", "D"]
upper_list = []
for 대문자 in my_list:
    if 대문자.isupper():
        upper_list.append(대문자)
print(upper_list)

# 149
my_list = [3, 4, 4, 5, 6, 6]
sole_list = []
for i in range(4):
    sole_list.append(my_list[i])
    if my_list[i] == my_list[i+1]:
        del my_list[i]
    else:
        pass
print(sole_list)
# 리스트여서 같은걸 가리키고 있는건가

# 150
my_list = [3, 4, 5]
hap = 0
for i in range(len(my_list)):
    hap += int(my_list[i])
print(hap)
