a = [1, 9, 8, 4, 5, 11, 5, 8, 9]
n = len(a)

summ = 0
for i in range(n):
    if a[i] % 2 == 1:
        summ = summ + a[i]
        i = i + 1
    else: i = i + 1
print("Сумма нечетных элементов массива:", summ)
