#!/bin/bash
for (( i = 1; i <= $1; i++ )); do
	echo Run $i/$1
	./run_test.sh $2
done
# find the maximum maxima
./maximum.py < maxima.txt
# average the averages
./average.py < averages.txt
