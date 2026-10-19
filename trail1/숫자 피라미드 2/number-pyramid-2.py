n = int(input())

cnt = 0

for i in range(1, n+1):
    cnt = cnt + i -1
    for j in range(1, i+1):
        print(cnt+j, end = " ")
    print()