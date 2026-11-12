n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
min = arr[0]
cnt = 0

for i in arr[1:]:
    if i < min:
        min = i

for i in arr:
    if min == i:
        cnt += 1

print(min, cnt)