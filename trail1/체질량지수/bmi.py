h, w =map(int, input().split())

bmi = int((10000*w)/(h*h))

if bmi >= 25:
    print(f"{bmi}\nObesity")
else:
    print(bmi)