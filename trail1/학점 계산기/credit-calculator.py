n = int(input())
arr = list(map(float, input().split()))

if sum(arr)/len(arr) >= 4.0:
    print(f'{sum(arr)/len(arr):.1f}')
    print("Perfect")
elif sum(arr)/len(arr) >= 3.0:
    print(f'{sum(arr)/len(arr):.1f}')
    print("Good")
else:
    print(f'{sum(arr)/len(arr):.1f}')
    print("Poor")
