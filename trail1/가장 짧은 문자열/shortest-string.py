a = input()
b = input()
c = input()

arr = [len(a), len(b), len(c)]

for i in range(3):
    for j in range(3):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(abs(arr[0]-arr[2]))