start, end = map(int, input().split())

# Please write your code here.

arr = 0

for i in range(start, end+1):
    cnt = -i
    for j in range(1, i+1):
        if i%j == 0:
            cnt += j
        else:
            pass
    if cnt == i:
        arr += 1
    else:
        pass

print(arr)