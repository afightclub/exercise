n = int(input())
arr = list(map(int, input().split()))
at = []

for i in arr:
    if i%2 == 0:
        at.append(i)

print(*at[::-1])