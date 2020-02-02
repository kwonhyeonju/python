# 051
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 052
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

# 053
print(nums[1::2])

# 054
nums2 = [1, 2, 3, 4, 5]
print(nums[::-1])

# 055
interest = ['삼성전자', 'lg전자', 'Naver']
print(interest[0], interest[2])
print(interest[::2])  # 이거 틀림!!


# 056
interest2 = ['삼성전자', 'lg전자', 'Naver', 'sk하이닉스', '미래에셋대우']
print(interest2[0], interest2[1], interest2[2], interest2[3], interest2[4])
# 이거 말고 다른방법이 있나...?
# .join()을 이용해 ' '을 삽입할 수 있다
print(interest2.join())

# 057
# print(interest2[0]'/'interest[1]'/'interest2[2]'/'interest2[3]'/'interest2[4])
# 다른방법이 있을것 같은데..
# ㅋㅋㅋㅋㅋ틀림
# print(interest2.join('/'))

# 058
print('\n'.join(interest2))

# 059
string = "삼성전자/lg전자/naver"
interest3 = []
interest3 = string.split('/')
print(interest3)
# 답지랑 다른방식

# 60
string2 = "삼성전자/lg전자/navre/sk하이닉스/미래에셋대우"
interest4 = []
interest4 = string2.split('/')
print(interest4)
