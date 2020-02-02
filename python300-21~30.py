# 021
lang = 'python'
print(lang[0], lang[2])

# 022
license_plate = "24가 2210"
print(license_plate[-1:-4])
print(license_plate[-4:])
print(license_plate[-4:0])
print(license_plate[4:8])

# 023
string = "홀짝홀짝홀짝"
print(string[::2])
print(string[-6:0])

# 024
# 증감폭을 음수로 지정하면 역순으로 문자들을 가져온다.
# print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))


# 026
# ? sep='' sep기능이 뭐죠?
# print(phone_number.replace('-', '')) <- 이렇게도 가능

# 027
url = "http://sharebook.kr"
print(url[-1:-2])
print(url[-2:])

# 028
# python
# ?????
#!!! type error 'str' 기존에 생성한 문자열은 변경할 수 없다

# 029
string = 'abcdfe2a35323a'
#print(string.upper())
print(string.replace('a', 'A'))
#print(string[-3:-2])  # 2
#print(string[-3:-1])  # 23
print(string)

string = string.replace('a', 'A')
print(string)

# 030
# abcd
