sum = 0
len = 0

for _ in range(10):
    a = int(input())
    if 0 <= a <= 200:
        sum += a
        len += 1

print('%d %.1f' %(sum, sum/len))