N = int(input("Введите число N: "))
for i in range(1, N+1):
    Ni = int(input("Введите число: "))

max_v = 0

for i in range(1, N+1):
    if max_v < Ni:
        max_v = Ni
        i = i + 1
    else: i = i + 1

print("Наибольшее число:", max_v)



