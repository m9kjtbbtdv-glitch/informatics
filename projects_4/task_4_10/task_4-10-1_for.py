N = int(input("Введите число N: "))

factor = 1

for i in range(1, N):
    factor = factor * i

print("Факториал числа:", factor)
