x = float(input("Введите число X: "))
y = float(input("Введите число Y: "))
z = float(input("Введите число Z: "))
w = float(input("Введите число W: "))

if x < y:
    if x < z:
        if x < w:
            min_v = x
        else: min_v = w
    else: 
        if z < w:
            min_v = z
        else: min_v = w
else:
    if y < z:
        if y < w:
            min_v = y
        else: min_v = w
    else: 
        if z < w:
            min_v = z
        else: min_v = w

print("Максимальное число:", min_v)
