a, b = map(int, input().split())

arr = []

while a > 1:
    arr.append(a%b)
    a = a//b

cnt = 0

for i in range(b):
    cnt += arr.count(i) ** 2

   
print(cnt)