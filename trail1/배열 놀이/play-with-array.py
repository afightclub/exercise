n, q = map(int, input().split())

seq = list(map(int, input().split()))

for i in range(q):
    qipt = list(map(int, input().split()))

    if qipt[0] == 1:
        print(seq[qipt[1]-1])
    elif qipt[0] == 2:
        if qipt[1] not in seq:
            print(0)
        elif qipt[1] in seq:
            for j in range(n):
                if seq[j] == qipt[1]:
                    print(j+1)
                    break
    elif qipt[0] == 3:
        print(*seq[qipt[1]-1:qipt[2]])