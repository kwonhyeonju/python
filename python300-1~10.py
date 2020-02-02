# 001
print("Hello World")

# 002
print("Mary\'s cosmetics")

# 003
print("신씨가 소리질렀다. \"도둑이야\".")
#print('신씨가 소리질렀다. "도둑이야".')

# 004
print("C:\Windows")

# 005
# \n : 줄바꿈    \t: 탭

# 006
# 오늘은일요일
# 정답 : 오늘은 일요일 (사이에 공백이 생김)

# 007~008 다시하기-----------------
# 007
# print에 sep옵션을 이용하여 다른문자를 넣을 수 있음(공백포함) sep=" "   //print("안녕","하세요", sep="!")

# end옵션 :
# end옵션은 뒤의 출력값과 이어지게 해줌.
# end="" : sep과 같은 기능을 함. 문장을 출력하고 마지막에 무엇을 쓰고 끝낼지 정해줌 (이스케이프문자 포함)
print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep=";")
print("naver""kakao""sk""samsung")  # ,를 없애면 공백이 사라짐

# 008
print("naver//kakao//sk//samsung")
#print("naver", "kakao", "sk", "samsung", sep="/")


# 009
print("first")
print("second")
print("first", end=' ')
print("second", end='\n')


# ----------------------------------

# 010
string = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"
print(len(string))
