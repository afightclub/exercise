n, m = map(int, input(). split())
seq = list(map(int, input().split()))
cnt = 0

for i in seq:
    if i == m:
        cnt += 1
print(cnt)