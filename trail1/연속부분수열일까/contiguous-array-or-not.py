n1, n2 = map(int, input().split()) # 4, 2     //10 6
# 어떻게 비교할 수 있을까? 하나씩 비교는 할 수 있을 거 같은데 두 개를 어떻게? 하니씩 비교해야 하나?
a = list(map(int, input().split())) # 1 5 2 6 //9 2 4 1 3 3 1 4 6 8
b = list(map(int, input().split())) # 5 6 //    4 1 3 3 1 4 아래를 일반화 하면 됨
cnt = 0
for i in range(n1-n2+1):
    sl = a[i:n2+i]
    if sl == b:
        cnt +=1
        break

if cnt == 1:
    print("Yes")
else:
    print("No")