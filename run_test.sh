#!/bin/bash
./test.sh $1 | tail -n2 | awk '{print $3}' > temp.txt
head -n1 temp.txt >> maxima.txt
tail -n1 temp.txt >> averages.txt
rm temp.txt
