cnt = 0
len = 0

while True:
    n = int(input())
    if 20<= n <=29:
        cnt += n
        len += 1
    else:
        print("%.2f" %(cnt/len))
        break