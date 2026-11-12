n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_val = [0]

for i in range(n):  # 10 5 6 5
    for j in range(n-1, i,-1):
        if price[i] < price[j]:
            max_val.append(price[j] - price[i])

print(max(max_val))