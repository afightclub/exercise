n = int(input())

arr1 = [
    [1 for _ in range(i)]
    for i in range(1, n+1)
] 

for i in range(n):
    for j in range(i):
        if i >= 1 and j >=1 :
            arr1[i][j] = arr1[i-1][j-1] + arr1[i-1][j]

for row in range(n):
    print(*arr1[row])