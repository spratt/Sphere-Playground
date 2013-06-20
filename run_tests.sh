#!/bin/bash
# Runs a given number of tests with a given number of points, then
# aggregates the maxima and averages
for (( i = 1; i <= $1; i++ )); do
	echo Run $i/$1
	./run_test.sh $2
done
# find the maximum maxima
./maximum.py < maxima.txt
# average the averages
./average.py < averages.txt
