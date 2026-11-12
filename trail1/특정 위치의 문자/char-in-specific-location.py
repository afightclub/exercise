ipt = input()
word = ['L', 'E', 'B', 'R', 'O', 'S']
idx = -1

for i in range(len(word)):
    if word[i] == ipt:
        idx = i

if idx == -1:
    print('None')
else:
    print(idx)