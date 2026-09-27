a, b = map(int, input().split())

print(a//b, end = ".")

r = a%b

for i in range(20):
    r *= 10
    d = r // b
    print(d, end = "")
    r = r % b