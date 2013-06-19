#!/usr/bin/env python2.6
from sys import stdin

total = 0
n = 0

for line in stdin:
    n += 1
    total += float(line.strip())

print total / n
