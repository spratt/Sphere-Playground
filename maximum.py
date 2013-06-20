#!/usr/bin/env python2.6
"""
maximum.py
By Simon Pratt

Given one floating-point number per line of input, calculates and
prints the maximum of the numbers.
"""
from sys import stdin, maxint

max_so_far = -maxint-1

for line in stdin:
    n = float(line.strip())
    if n > max_so_far:
        max_so_far = n

print max_so_far
