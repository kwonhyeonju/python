# 큰수 A+B
a = input("")
b = a.split(" ")
A = int(b[0])
B = int(b[1])
if (A > 0) & (B < 10**10000):
    print(A+B)
