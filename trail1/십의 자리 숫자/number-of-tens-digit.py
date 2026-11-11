num = list(map(int, input().split()))

for i in range(1, 10):
    cnt = 0
    for j in num:
        if j//10 == i:
            cnt += 1
        elif j == 0:
            break
        
    print(f'{i} - {cnt}')