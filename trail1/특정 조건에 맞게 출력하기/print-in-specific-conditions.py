n = list(map(int, input().split()))
arr = []

for i in n:
    if i%2 == 0 and i != 0:
        arr.append(i//2)
    elif i%2 != 0:
        arr.append(i+3)
    elif i == 0:
        break
print(*arr)