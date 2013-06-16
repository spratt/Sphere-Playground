#!/usr/bin/env python2.6
"""
all_pairs.py

By Simon Pratt

Given the output of rbox followed by a list of edges, compute
all-pairs shortest paths on the edges.
"""
import numpy as np
from sys import stdin

lines = []

for line in stdin:
    lines.append(line.strip())

lines.pop(0)

n = int(lines.pop(0))
vertices = []

while n > 0:
    n -= 1
    vertices.append(tuple(lines.pop(0).split(' ')))

edges = []
    
for line in lines:
    edges.append(tuple(lines.pop(0).split(' ')))

dists = np.empty((n,n))

INFINITY = -1

for row in range(n):
    for col in range(n):
        dists[row][col] = INFINITY
