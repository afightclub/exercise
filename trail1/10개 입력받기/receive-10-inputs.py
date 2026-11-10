a = list(map(int, input().split()))
arr = []
for i in a:
    if i == 0:
        break
    arr.append(i)

print(f"{sum(arr)} {sum(arr)/len(arr):.1f}")