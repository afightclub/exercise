start, end = map(int, input().split())

# Please write your code here.

arr = 0

for i in range(start, end+1):
    cnt = 0
    for j in range(1, i):
        if i%j == 0:
            cnt += j
        else:
            pass
    if cnt == i:
        arr += 1
    else:
        pass

print(arr)