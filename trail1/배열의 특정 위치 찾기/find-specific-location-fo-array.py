arr = list(map(int, input().split()))
n = len(arr)

arr1 = sum(arr[1::2])
arr2 = sum(arr[2::3])/3

print(f'{arr1} {arr2:.1f}')