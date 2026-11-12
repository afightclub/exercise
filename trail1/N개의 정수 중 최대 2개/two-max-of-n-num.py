n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max1 = a[0]
max2 = a[1]

for i in a[2:]:
    if max1 < i:
        max2 = max1
        max1 = i 
    elif max2 < i:
        max2 = i

print(max1, max2)