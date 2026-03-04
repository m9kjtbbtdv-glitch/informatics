#!/bin/bash
if [ $# -ge 2 ]; then
    name="$1"
    level="$2"
else
    echo "Недостаточно аргументов"
    read -p "Введите имя гена: " name
    read -p "Введите уровень экспрессии (целое число): " level
fi

echo "Экспрессия гена $name составляет $level единиц"
