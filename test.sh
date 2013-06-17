#!/bin/bash
./gen_points.sh 30 $1 > points.txt
cat points.txt | qhull i | ./facets_to_edges.py | cat points.txt - | ./all_pairs.py
rm points.txt
