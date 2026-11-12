n = int(input())

nums = list(map(int, input().split()))

minmin = 100

for i in range(n):
    for j in range(i+1, n):
        if  nums[j] - nums[i] >= 0:
            min =  nums[j] - nums[i]
            if minmin > min:
                minmin = min

print(minmin)