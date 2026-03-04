
read -p "Введите массу (в кг): " mass
read -p "Введите рост (в метрах): " height
bmi=$(awk "BEGIN {printf \"%.0f\", $mass / ($height * $height)}")
echo "Ваш индекс массы тела: $bmi"

