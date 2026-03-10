df | awk 'NR > 1 {
    if ($5 > 90)
        print "WARNING:", $1, $5"%"
    else
        print $1, $5"%"
}'
