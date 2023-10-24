#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    a=1
    i=0
    x=True
    while x:
        if i==0 and i<n:
            a+=1
            i+=1
        if i<n:
            a+=1
            i+=1
        if i<n:
            a*=2
            i+=1
        if i>=n:
            x=False
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()

