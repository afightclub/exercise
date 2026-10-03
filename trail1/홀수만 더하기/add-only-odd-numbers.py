n = int(input())
sum = 0

for _ in range(n):
    z = int(input())
    if z%2 != 0 and z%3 == 0:
        sum += z

print(sum)