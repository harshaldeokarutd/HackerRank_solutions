#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
 x = s.split(" ")[0]
 y = s.split(" ")[1]
 test1 = ""
 test2 = ""
 for i in range(len(x)):
    if i == 0:
        test1 = x[0].upper( )
    else:
        test1 = test1 + x[i]

 for j in range(len(y)):
    if j == 0:
        test2 = y[0].upper()
    else:
        test2 = test2 + y[j]

 return test1 + " " + test2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
