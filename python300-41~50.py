# 041
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 042
movie_rank.append("배트맨")
print(movie_rank)

# 043
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
# ? 0부터 시작하겠지?=> 맞음

# 044
movie_rank.remove("럭키")
print(movie_rank)
#----del movie_rank[3]도 가능-------

# 045
del movie_rank[2:]  # del은 del.으로 사용안함
print(movie_rank)

# 046
lang1 = ["c", "c++", "java"]
lang2 = ["python", "Go", "c#"]
langs = lang1+lang2
print(langs)

# 047
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))

# 048
nums2 = [1, 2, 3, 4, 5]
print(nums2[0]+nums2[1]+nums2[2]+nums2[3]+nums2[4])
# for문은 틀림
a=0
for num in nums2:
    print(num)
    # a = 0  # a=0이란 값을 선언을 해줘야 하겠지?=>멍청이네 ㅋㅋㅋ 안에다가 선언해줌
    print("a값: ", a)
    a = num+a
    print("더한후 a값: ", a)
print(a)
#----------sun()이라는 함수가 있음 ==> print(sum(nums))------------



# 049
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 50
nums3 = [1, 2, 3, 4, 5]
print(float((nums3[0]+nums3[1]+nums3[2]+nums3[3]+nums3[4])/len(nums3)))
#----print(sun(nums)/5)----
