n = int(input())
arr = []
i = 1 
cnt = 0

while cnt < 2:
    arr.append(n*i)
    if (n*i)%5 == 0:
        cnt += 1
    i += 1

print(*arr)