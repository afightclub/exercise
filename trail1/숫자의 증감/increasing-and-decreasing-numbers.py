c, n = input().split()
N = int(n)
if c == "A":
    for i in range(1, N+1):
        print(i, end = " ") 
else:
    for i in range(N, 0, -1):
        print(i, end= " ")