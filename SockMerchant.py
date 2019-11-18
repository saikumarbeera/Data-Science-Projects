#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    d = defaultdict(int)
    for k in ar:
        d[k] += 1
    for x, y in d.items():
        print(x, y) 
    cnt = 0
    for ele in d.values():
        print(ele)
        cnt += ele//2
        print(cnt)
    print(d.values())
    return cnt
           

def main():
    #fptr = open(os.environ['OUTPUT_2PATH'], 'w')
    fptr = sys.stdout

    totalElements = int(input()) # Number of elements in the input

    inputArray = list(map(int, input().rstrip().split())) # Input in sequential order
    #inputArray.append('#')
    

    result = sockMerchant(totalElements, inputArray)
    print (inputArray)

    fptr.write(str(result) + '\n')

    fptr.close()


if __name__ == "__main__":
    main()
    