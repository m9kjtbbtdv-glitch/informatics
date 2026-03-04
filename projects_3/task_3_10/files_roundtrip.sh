#!/bin/bash

echo "Создание файлов:"
for i in {1..10}; do
    touch "test${i}.txt"
    echo "Создан test${i}.txt"
done

echo -e "\nУдаление файлов в обратном порядке:"
n=10
while [ $n -ge 1 ]; do
    rm "test${n}.txt"
    echo "Удалён test${n}.txt"
    n=$((n - 1))
done
