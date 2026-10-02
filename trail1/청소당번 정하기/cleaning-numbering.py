# 2일마다 교실
# 3일마다 복도
# 12일마다 화장실
# 겹치면 주기가 더 긴 것

n = int(input())

cnt1 = 0
cnt2 = 0
cnt3 = 0


for i in range(1, n+1):
    if i%12 == 0:
        cnt3 += 1
    elif i%3 == 0:
        cnt2 += 1
    elif i%2 == 0:
        cnt1 += 1
    
print(cnt1, cnt2, cnt3)