g = input()
o = input()
cnt = 0

for i in range(len(g)):
    if g[i] == o:
        cnt += 1

print(cnt)