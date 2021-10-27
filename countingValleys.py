#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def counting_valleys(steps, path):    
    sealevel = 0
    inside_valley = 0
    valley_count = 0

    for i in range(steps):
        sealevel += ( -1 if path[i] == 'D' else 1 )

        if not inside_valley and sealevel < 0:
            valley_count += 1
        
        inside_valley = 1 if sealevel < 0 else 0

    return valley_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = counting_valleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
