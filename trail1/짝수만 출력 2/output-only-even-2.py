b, a = map(int, input().split())

i = b
while i >= a:
    if i%2 == 0:
        print(i, end = " ")
        i -= 2
    else:
        print("you have to input even number")