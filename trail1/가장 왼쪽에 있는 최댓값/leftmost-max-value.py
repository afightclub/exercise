n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max = 0
num = []

for i in range(n):
    if max < a[i]:
        max = a[i]
        num.append(i+1)

print(*num[::-1])
