#!/usr/bin/env python2.6
"""
facets_to_edges.py

By Simon Pratt

Converts the facets output of qhull to a list of edges.
"""
from sys import stdin

lines = []

for line in stdin:
    lines.append(line.strip())

lines.pop(0)

edges = set()

def str_edge(u,v):
    return '{0} {1}'.format(u,v)

def add_edge(u,v):
    if u < v:
        edges.add(str_edge(u,v))
    else:
        edges.add(str_edge(v,u))

for line in lines:
    a,b,c = map(int,line.split(' '))
    add_edge(a,b)
    add_edge(b,c)
    add_edge(c,a)

for edge in edges:
    print edge
