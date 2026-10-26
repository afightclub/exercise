n = int(input())

for _ in range(n):
    arr = input().split()
    cnt = 1
    a, b = int(arr[0]), int(arr[1])
    for i in range(a, b+1):
        cnt *= i
    print(cnt)