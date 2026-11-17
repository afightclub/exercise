n = int(input())

arr = [
    input()
    for _ in range(n)
]

cnt1 = 0
cnt2 = 0

for i in range(n):
    cnt1 += len(arr[i])
    if arr[i][0] == "a":
        cnt2 += 1

print(cnt1, cnt2)