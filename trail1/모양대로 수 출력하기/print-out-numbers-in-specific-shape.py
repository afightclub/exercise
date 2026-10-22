n = int(input())
cnt = -1

for i in range(n, 0, -1):
    cnt += 1
    for j in range(0, cnt):
        print(" ", end = " ")
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()