num = list(map(int, input().split()))
min = num[0]
max = 0

for i in num:
    if max < i and i != 999:
        max = i
    elif min > i and i != -999:
        min = i

print(max, min)