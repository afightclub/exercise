n, m = map(int, input().split())

# Please write your code here.
#1) 먼저 채우고 바꾸기
#2) 세로부터 채우기 >> 가능한가?

arr1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]
num = 0
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            arr1[j][i] = num
            num += 1
    else:
        for j in range(n-1, -1, -1):
            arr1[j][i] = num
            num += 1

for i in range(n):
    print(*arr1[i])