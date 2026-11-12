n = int(input())
seq = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
t = 0

for i in seq:
    if i == 2:
        cnt1 += 1
    cnt2 += 1
    if cnt1 == 3:
        t = cnt2
        break

print(t)
    