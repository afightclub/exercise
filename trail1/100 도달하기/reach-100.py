n = int(input())
seq = [1, n]
i = 0

while seq[i+1]<100:
    seq.append(seq[i]+seq[i+1])
    i += 1

print(*seq)