#!/usr/bin/env python2.6
from sys import stdin, maxint

max_so_far = -maxint-1

for line in stdin:
    n = float(line.strip())
    if n > max_so_far:
        max_so_far = n

print max_so_far
