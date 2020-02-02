# 5번
#실행결과 : [[1,4,7], [2,5,8], [3,6,9]]

numbers = [1, 2, 3, 4, 5, 6, 7]
output = [[], [], []]
print(output[0], output[1], output[2])

for number in numbers:
    print(number)

    output[number-1 % 3].append(number)

    print(output)
