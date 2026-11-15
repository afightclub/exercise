n = 5

arr1 = [
    [1 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, n):
    for j in range(1,n):
        arr1[i][j] = arr1[i][j-1] + arr1[i-1][j]

for i in range(n):
    print(*arr1[i])