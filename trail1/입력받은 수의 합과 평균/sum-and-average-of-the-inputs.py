n = int(input())
sum = 0
len = 0
for i in range(n):
    a = int(input())
    sum += a
    len += 1

print('%d %.1f' %(sum, sum/len))