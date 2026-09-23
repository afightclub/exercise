a = input().split()
b = input().split()
c = input().split()

a1 = str(a[0])
b1 = str(b[0])
c1 = str(c[0])

a2 = int(a[1])
b2 = int(b[1])
c2 = int(c[1])

if a1 == "Y" and a2 >= 37:
    if (b1 == "Y" and b2 >= 37) or (c1 == "Y" and c2 >= 37):
        print("E")
    else:
        print("N")
elif b1 == "Y" and b2 >= 37:
    if c1 == "Y" and c2 >= 37:
        print("E")
    else:
        print("N")
else:
    print("N")