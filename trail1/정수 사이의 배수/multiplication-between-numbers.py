a, b = map(int, input().split())
sum = 0 
len = 0

for i in range(a, b+1):
    if i%5 == 0 or i%7 == 0:
        sum += i
        len += 1

avr = sum/len

print('%d %.1f' %(sum, avr))