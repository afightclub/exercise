a = input().split()
b = input().split()

a1 = int(a[0])
b1 = int(b[0])
a2 = str(a[1])
b2 = str(b[1])

if (a1 >= 19 and a2 == "M") or (b1 >= 19 and b2 == "M"):
    print(1)
else:
    print(0)