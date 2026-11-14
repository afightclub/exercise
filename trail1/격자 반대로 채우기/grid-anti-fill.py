n = int(input())

arr1 = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

if n%2 == 0:
    for i in range(n-1, -1, -1):
        if i%2 != 0:
            for j in range(n-1, -1, -1):
                arr1[j][i] = num
                num += 1
        else:
            for j in range(n):
                arr1[j][i] = num
                num += 1
else:
    for i in range(n-1, -1, -1):
        if i%2 == 0:
            for j in range(n-1, -1, -1):
                arr1[j][i] = num
                num += 1
        else:
            for j in range(n):
                arr1[j][i] = num
                num += 1

for row in range(n):
    print(*arr1[row])