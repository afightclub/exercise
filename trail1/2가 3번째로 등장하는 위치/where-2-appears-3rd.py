n = int(input())
seq = list(map(int, input().split()))
cnt = 0
for i in range(len(seq)):
    if seq[i] == 2:
        cnt += 1
        if cnt == 3:
            print(i+1)