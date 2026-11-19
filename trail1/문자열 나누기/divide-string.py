n = int(input())
a_str = input().split()
b_str = ""

for i in range(n):
    for j in range(len(a_str[i])):
        if len(b_str)%6 == 0:
            b_str += "\n"
        b_str += a_str[i][j]


        


print(b_str.lstrip())