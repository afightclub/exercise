n = int(input())

arr1 = []

for i in range(1, n+1):
    arr2 = []
    for j in range(n):
        arr2.append(i+n*j)
    arr1.append(arr2)

for i in range(n):
    print(*arr1[i])