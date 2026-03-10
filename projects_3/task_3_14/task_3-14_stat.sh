awk '{sum += $2} END {print "Sum:", sum}' students.txt
awk '{sum += $2; n++} END {print "Average:", sum/n}' students.txt
awk 'NR==1{max=$2} $2>max{max=$2} END {print "Max:", max}' students.txt
