arr = [0]*4

for i in range(3):
    h = input().split()
    h[1] = int(h[1])
    if h[0] == "Y" and h[1] >= 37:
        arr[0] += 1
    elif h[0] == "N" and h[1] >= 37:
        arr[1] += 1
    elif h[0] == "Y" and h[1] < 37:
        arr[2] += 1
    elif h[0] == "N" and h[1] < 37:
        arr[3] += 1

if arr[0] >= 2:
    arr.append("E")
    
print(*arr)