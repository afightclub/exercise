n = int(input())
cnt = 0

for i in range(1, n+1):
    cnt += 1
    if n//i > 1:
        n = n//i
        continue
    else:
        break

print(cnt)