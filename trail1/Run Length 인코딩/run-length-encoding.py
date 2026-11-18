A = input()

result = ""
cnt = 1

for i in range(1, len(A)):
    if A[i] == A[i-1]:
        cnt += 1
    else:
        result += A[i-1] + str(cnt)

        cnt = 1

result += A[-1] + str(cnt)

print(len(result))
print(result)