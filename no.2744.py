# BAEKJOON - 파이썬으로 쉽게 푸는 문제
# 2744
'''
영어소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 변환하는 프로그램을 작성하시오
'''
string = input("")
for i in string:
    if i.isupper():
        print(i.lower(), end="")
    else:
        print(i.upper(), end="")
