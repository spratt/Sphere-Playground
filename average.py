#!/usr/bin/env python2.6
"""
average.py
By Simon Pratt

Given one floating-point number per line of input, calculates and
prints the average of the numbers.
"""
from sys import stdin

total = 0
n = 0

for line in stdin:
    n += 1
    total += float(line.strip())

print total / n
