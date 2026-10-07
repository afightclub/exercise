s = True

for _ in range(5):
    t = int(input())
    if t%3 != 0:
        s = False

if s == False:
    print(0)
else:
    print(1)