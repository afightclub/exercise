p = list(map(int, input().split()))

for i in range(8):
    p.append((p[i]+p[i+1])%10)

print(*p)