apd = list(map(int, input().split()))

arr = []

for i in apd:
    if i == 0:
        break
    arr.append(i)

print(*arr[::-1])