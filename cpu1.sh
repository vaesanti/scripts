###########################
#!/usr/bin/env bash

file=/proc/stat

#used_perc=$(grep -w cpu $file | awk '{used=$2+$3+$4+$7+$8; total=used+$5+$6; printf "%d", used*100/total}')
used_perc=$[100-$(vmstat 1 2|tail -1|awk '{print $15}')]

echo "cpu is "$used_perc%

#########################