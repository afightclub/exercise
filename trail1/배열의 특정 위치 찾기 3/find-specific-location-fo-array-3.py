a = list(map(int, input().split()))
l = len(a)
t = 0
for i in range(0, l):
    if a[i] == 0:
        t = a[i-1] + a[i-2] + a[i-3]
        break
    else:
        pass
print(t)