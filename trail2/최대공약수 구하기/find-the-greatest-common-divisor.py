n, m = map(int, input().split())

# Please write your code here.

def max_de(n, m):
    while m != 0:
        n, m = m, n % m 
    print(n)

max_de(n, m)