#!/usr/bin/env python2.6
"""
all_pairs.py

By Simon Pratt

Given the output of rbox followed by a list of edges, compute
all-pairs shortest paths on the edges.
"""
import numpy as np
from sys import stdin, maxint, exit
from math import sqrt

lines = []

for line in stdin:
    lines.append(line.strip())

print lines.pop(0)

n = int(lines.pop(0))
vertices = []

for _ in range(n):
    vertices.append(tuple(map(float,lines.pop(0).split(' '))))

edges = []
    
for line in lines:
    edges.append(tuple(map(int,lines.pop(0).split(' '))))
    
dists = np.empty((n,n))

INFINITY = maxint

# distance defaults to infinity
for row in range(n):
    for col in range(n):
        dists[row][col] = INFINITY

# distance from node to itself is zero
for i in range(n):
    dists[i][i] = 0

square = lambda x: x * x

def get_dist(u,v):
    return sqrt(square(vertices[u][0] - vertices[v][0]) +
                square(vertices[u][1] - vertices[v][1]))
    
# input edge distances
for edge in edges:
    u = edge[0]
    v = edge[1]
    d = get_dist(u,v)
    dists[u][v] = d
    dists[v][u] = d

# floyd-warshall all-pairs shortest path algorithm
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dists[i][k] + dists[k][j] < dists[i][j]:
                dists[i][j] = dists[i][k] + dists[k][j]

# print the distances
print "| u | v | d_e | d_g |  t  |"
print "+---+---+-----+-----+-----+"

for i in range(n):
    for j in range(i+1,n):
        de = get_dist(i,j)
        dg = dists[i][j]
        t = dg / de
        print "|%(u)3d|%(v)3d|%(de)5.2f|%(dg)5.2f|%(t)5.2f|" % {"u":i,"v":j,"de":de,"dg":dg,"t":t}

print "+---+---+-----+-----+-----+"
