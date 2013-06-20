#!/bin/bash
# Generate a given number of points with an optional timestamp seed,
# compute the convex hull on those points, translate the facets to
# edges, then run Floyd-Warshall all-pairs shortest path to calculate
# the spanning ratio between all pairs
./gen_points.sh $1 $2 > points.txt
cat points.txt | qhull i | ./facets_to_edges.py | cat points.txt - | ./all_pairs.py
rm points.txt
