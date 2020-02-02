# 순서와 변수에 들어있는 값을 생각하면서 진행

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for a in list_of_list:
    for b in a:
        print(b)

print("프로그램이 종료되었습니다.")
