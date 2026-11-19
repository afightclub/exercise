given_str = input()

cho  = ""

for i in range(len(given_str)):
    if i%2 != 0:
        cho += given_str[i]

print(cho[::-1])
        