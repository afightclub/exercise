n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

max = -1

for i in nums:
    cnt = 0

    for j in nums:
        if i == j:
            cnt += 1
    
    if cnt < 2 and max < i:
        max = i


print(max)