seq = list(map(int, input().split()))

for i in range(8):
    seq.append(seq[i+1]+(seq[i]*2))

print(*seq)