#!/bin/bash
# This program generates points on a unit sphere using the rbox
# program, part of the qhull package.
if [[ $# -lt 1 ]]; then
	echo "Usage: $0 num_points"
	exit
fi
rbox $1 D3 s B1.0