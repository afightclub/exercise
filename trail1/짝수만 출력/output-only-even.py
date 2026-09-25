a, b = map(int, input().split())

i = a

while i >= a and i <= b:
    if i%2 ==0:
        print(i, end = " ")
    i += 2