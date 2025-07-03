#!/bin/bash

# Simple Interest Calculator

echo "Enter Principal amount:"
read p
echo "Enter Rate of interest:"
read r
echo "Enter Time (in years):"
read t

si=$(echo "scale=2; ($p * $r * $t) / 100" | bc)
echo "Simple Interest is: $si"
