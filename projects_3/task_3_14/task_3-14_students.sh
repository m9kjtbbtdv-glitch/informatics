#!/bin/bash

echo "Имена студентов:"
cut -d' ' -f1 students.txt

echo "Оценки студентов:"
cut -d' ' -f2 students.txt

echo "Номер строки и имя:"
awk '{print NR, $1}' students.txt
