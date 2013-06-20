#!/usr/bin/env python2.6
"""
calc_distances.py
By Simon Pratt

Calculates the distance from origin of points generated using rbox,
part of the qhull package.
"""
from sys import stdin
from math import sqrt, pow

lines = []

for line in stdin:
    lines.append(line.strip())

print lines.pop(0)
print lines.pop(0)

distances = []

for line in lines:
    parts = line.split(' ')
    a,b,c = map(float,parts)
    dist = sqrt(pow(a,2) + pow(b,2) + pow(c,2))
    distances.append(dist)
    print line
    print dist

avg = reduce(lambda x,y: x+y, distances) / len(distances)
print "Average: {0}".format(avg)
