#!/bin/bash
# Runs a single test with a given number f points, printing the
# maximum to a file and the average to another file
./test.sh $1 | tail -n2 | awk '{print $3}' > temp.txt
head -n1 temp.txt >> maxima.txt
tail -n1 temp.txt >> averages.txt
rm temp.txt
