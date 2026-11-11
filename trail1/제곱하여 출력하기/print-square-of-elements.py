n = int(input())
arr = map(int, input().split())

new_arr = [i*i for i in arr]
print(*new_arr)