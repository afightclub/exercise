arr1 = []
t = 0
for i in range(2):

    arr = list(map(int, input().split()))
    arr1.append(arr)
    t += sum(arr)

    print(f'{sum(arr)/len(arr):.1f}', end = " ")
print()

for i in range(4):
    arr2 = []
    for j in range(2):
        arr2.append(arr1[j][i])
        
    print(f'{sum(arr2)/len(arr2):.1f}', end = " ")
print()

print(f'{t/8:.1f}')