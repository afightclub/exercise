n, m = map(int, input().split())

# Please write your code here.

arr1 = [
    [ 0 for i in range(m)] #열
    for j in range(n) #행
]

num = 1

for k in range(n+m-1):
    for i in range(n):
        for j in range(m):
            if i + j == k:
                arr1[i][j] = num
                num += 1

for row in range(n):
    print(*arr1[row])