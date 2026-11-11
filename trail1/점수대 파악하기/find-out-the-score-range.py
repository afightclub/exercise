score = list(map(int,input().split()))

for i in range(10, 0, -1):
    cnt = 0
    for j in score:
        if j//10 == i:
            cnt += 1
        elif j == 0:
            break
    print(f'{i*10} - {cnt}')