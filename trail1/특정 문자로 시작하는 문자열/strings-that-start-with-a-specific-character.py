n = int(input())

txt = [
    input()
    for _ in range(n)
]

word = input()

cnt1 = 0
cnt2 = 0

for i in range(n):
    if txt[i][0] == word:
        cnt1 += 1
        cnt2 += len(txt[i])

print(f'{cnt1} {cnt2/cnt1:.2f}')