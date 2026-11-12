n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min = arr[0]
cnt = 1

for i in range(1, n):
    if min > arr[i]:
        min = arr[i]
        cnt = 1
    elif min == arr[i]:
        cnt += 1
print(min, cnt)