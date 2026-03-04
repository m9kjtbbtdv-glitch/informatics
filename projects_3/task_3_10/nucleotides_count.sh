#!/bin/bash
printf "%-15s %-5s %-5s %-5s %-5s\n" "Файл" "A" "T" "G" "C"
printf "%-15s %-5s %-5s %-5s %-5s\n" "---------------" "-----" "-----" "-----" "-----"

for file in *.fasta; do
    [ -e "$file" ] || continue

    [ -s "$file" ] || continue

    a=0; t=0; g=0; c=0

    while IFS= read -r line; do
        if [[ $line == \>* ]]; then
            continue
        fi
        for (( i=0; i<${#line}; i++ )); do
            char="${line:$i:1}"
            case $char in
                [Aa]) ((a++)) ;;
                [Tt]) ((t++)) ;;
                [Gg]) ((g++)) ;;
                [Cc]) ((c++)) ;;
                *) ;; 
            esac
        done
    done < "$file"

    printf "%-15s %-5d %-5d %-5d %-5d\n" "$file" $a $t $g $c
done
