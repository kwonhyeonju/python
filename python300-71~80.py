# 074
temp = {}

# 075
icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# 가견은 숫자 그대로여서 ""가 없어도 됨

# 076
# ***
icecream["죠스바"] = 1200
icecream["월드콘"] = 1500

# 077
print("{} 가격: {}".format("메로나", icecream["메로나"]))

# 078
icecream.update("메로나": 1300)
print(icecream)

# 079
del icecream["메로나"]

# 080
# icecream안에 '누가바'라는 키가 존재하지 않아서
