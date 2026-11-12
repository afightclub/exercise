ipt = input()
word = ['L', 'E', 'B', 'R', 'O', 'S']
idx = -1

for i,char in enumerate(word):
    if char == ipt:
        idx = i

if idx == -1:
    print('None')
else:
    print(idx)