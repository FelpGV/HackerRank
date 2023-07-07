import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def splitLetter(s):
    return re.sub('\D', '', s)

def timeConversion(s):
    print(s[2:8])

    regularExpression = '^(0?[1-9]|1[0-2]):[0-5][0-9]:[0-5][0-9]([P][M])'
    a = []
    result = re.match(regularExpression, s)
    a = s.split(":")
    a = [splitLetter(s) for s in a]
    if(result != None):
        num = int(a[0])
        if(num != 12):
            sum = num+12
            a[0] = str(sum)
        else:
            a[0] = str(num)
    else:
        num = int(a[0])
        if(num == 12):
            sum = num-12
            a[0] = '0' + str(sum)
        else:
            a[0] = '0' + str(num)
    
    a = ':'.join(a)
    print(a)
    return s

if __name__ == '__main__':

    s = '04:59:59AM'

    result = timeConversion(s)

    
