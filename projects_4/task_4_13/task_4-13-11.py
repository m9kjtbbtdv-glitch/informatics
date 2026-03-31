a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)

j = 0
i = 1
even = 0

while (i < n):
        even = even + a[i]
        i = i + 2
        j = j + 1
even = even/j
print("Среднее арифметическое элементов с четными индексами массива:", even)
