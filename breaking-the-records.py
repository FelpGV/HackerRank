import math
import os
import random
import re
import sys


def breakingRecords(scores):
    min = 0
    max = 0
    minimun = scores[0]
    maximun = scores[0]
    for x in range(1,len(scores)):
        if(scores[x] > maximun):
            maximun = scores[x]
            max += 1
        if(scores[x] < minimun):
            minimun = scores[x]
            min += 1
    return (max,min)

if __name__ == '__main__':

    #n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    
