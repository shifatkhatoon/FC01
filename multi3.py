#!/bin/python3
import sys
# range na lekr % b use kr skte h.but runtime error aarha h or ek m timeout ho rha h 10s s.

multiple = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for num in range(0,n,3):
        multiple.append(num)
    for num in range(0,n,5):
        if num not in multiple:
            multiple.append(num)
    print(sum(multiple))
    multiple = []

