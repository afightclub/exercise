import sys

nums = list(map(int, input().split()))

max = 0
min = sys.maxsize

for i in nums:
    if max < i < 500:
        max = i
    elif 500 < i < min:
        min = i
print(max, min)