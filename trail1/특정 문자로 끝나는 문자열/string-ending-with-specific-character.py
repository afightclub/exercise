txt = [
    input()
    for _ in range(10)
]
word = input()
cnt= 0
for i in range(10):
    if txt[i][-1] == word:
        print(txt[i])
        cnt += 1

if cnt == 0:
    print("None")