n, m = map(int, input().split())

arr1 = [
    list(map(int, input().split()))
       for i in range(n)
]

arr2 = [
    list(map(int, input().split()))
       for i in range(n)
]

arr3 = []

for i in range(n):
    t = []
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            t.append(0)
        else:
            t.append(1)
    arr3.append(t)

for i in range(n):
    print(*arr3[i])