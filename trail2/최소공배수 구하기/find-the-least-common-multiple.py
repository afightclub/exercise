n, m = map(int, input().split())

# Please write your code here.
mul = n*m
def min_mul(n, m):
    
    while m != 0:
        n, m = m, n % m
    
    print(f'{mul/n:.0f}')

min_mul(n,m)