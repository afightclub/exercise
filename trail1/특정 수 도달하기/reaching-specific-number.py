arr = list(map(int, input().split()))

for i in range(10):
    if arr[i] >= 250:
        print(f'{sum(arr[:i])} {sum(arr[:i])/len(arr[:i]):.1f}')
        break

else:
    print(sum(arr), sum(arr)/len(arr))