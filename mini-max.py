
import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sumsArray = []
    sums = 0
    pos = 0
    for x in range(len(arr)):
        for y in range(len(arr)):
            if(x != y):
                sums += arr[y]
        sumsArray.append(sums)
        sums = 0
        pos += 1

    hold = [None]*int(len(arr)-3)

    aux = 0
    for x in range(len(sumsArray)):
        for y in range(len(sumsArray)):
            if sumsArray[x] < sumsArray[y]:
                aux = sumsArray[x]
                sumsArray[x] = sumsArray[y]
                sumsArray[y] = aux
            aux = 0

    arr.sort()
    hold = [None]*int(len(arr)-3)
    for i in range(0,len(arr)-3):
        print(  range(0,len(arr)-3))

        print(f'i: {i}')

        temp = 0
        for j in range(i,i+4):
            print( range(i,i+4))
            print(f'j: {j}')


            temp = temp + arr[j]
        hold[i] = temp

    print(hold[0],hold[-1])
    
    print(sumsArray[0], sumsArray[-1])
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)