arr = list(map(int, input().split()))

odd = arr[0] + arr[2] + arr[4] + arr[6] + arr[8]
even = arr[1] + arr[3] + arr[5] + arr[7] + arr[9]

if odd >= even:
    print(odd-even)
else:
    print(even-odd)