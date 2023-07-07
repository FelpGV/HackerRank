
def divisibleSumPairs(k, ar):
    # Write your code here
    sum = 0
    numSum = 0
    for x in range(len(ar)):
        for y in range(x+1,len(ar)):
            sum = ar[x] + ar[y]
            if(sum % k == 0):
                numSum += 1
            sum = 0

    return(numSum)

if __name__ == '__main__':

    k = 3

    ar = [1, 3, 2, 6, 1, 2]

    result = divisibleSumPairs(k, ar)
    print(result)