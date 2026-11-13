for i in range(5):
    arr = list(input().split())
    for j in range(3):
        arr[j] = arr[j].upper()
    print(*arr)