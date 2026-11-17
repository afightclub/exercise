s = input()
arr = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0

for i in range(5):
    if s == arr[i][2] or s == arr[i][3]:
        print(arr[i])
        cnt += 1
print(cnt)