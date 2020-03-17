def func(i):
    if i == 1:
        return 1
    else:
        return i * func(i-1)


print(func(5))
print(func)

'''
def check(x):
    if x >= 60:
        return 'pass'
    else:
        return 'fail'
'''


'''
power2 = lambda x:x**2
print(power2(10))

plus = lambda x,y: x+y
result = plus(20,30)
print(result)

'''


def power2(x): return x**2


print(type(power2))
print(power2)
print(power2(10))


def plus(x, y): return x+y


result = plus(20, 30)
print(result)

print(lambda x: x+10)
print(lambda: 10)


# 문제
# 1
def check_score(x):
    if x >= 60:
        return 'pass'
    else:
        return 'fail'


print(check_score(88))


def check_score(x): return 'pass' if x >= 60 else 'fail'


print(check_score(88))

print(check_score)

# 2


def add(n, m):
    return n+m


print(add(2, 3))

print((lambda n, m: n+m)(2, 3))

##
items = [1, 2, 3, 4, 5]
map_test = map(lambda x: x**2, items)
print("---")
print(next(map_test))
print(next(map_test))
print(next(map_test))
print(next(map_test))
print(next(map_test))

# map() 예제
# 1


def plus_ten(x):
    return x+10


print(list(map(plus_ten, [1, 2, 3])))

# 2
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x*y, a, b)))

# 3
li = [1, 2, 3]
#result = [1,4,9]
result = list(map(lambda i: i**2, li))

print(result)
