givens = input()
n = int(input())
reverse_givens = givens[len(givens)-n::]
if n < len(givens):
    print(reverse_givens[::-1])
else:
    print(givens[::-1])