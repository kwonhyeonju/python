# 081
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}

# 082
print("{} 원".format(inventory["메로나"][0]))
# ??

# 083
print("{} 원".format(inventory["메로나"][1]))
# ??

# 084
inventory["월드콘"] = [500, 7]
print(inventory)

# 085
icecream = {'탱크보이': 1200, "폴라포": 1200, "빵빠레": 1800, "월드콘": 1500, "메로나": 1000}
print(icecream.keys())

# 086
print(icecream.values())

# 087
print(sum(icecream.values()))

# 088
new_product = {"팥빙수": 2700, "아맛나": 1000}
icecream.update(new_product)
print(icecream)

# 089


# 090
# ?
data = ["09/05", '09/06', "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = {}
i = 0
for i in range(len(data)):
    close_table[data[i]] = close_price[i]
print(close_table)
#--zip()을 이용해서 할 수 있음--