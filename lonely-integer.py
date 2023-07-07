def lonelyinteger(a):
    numInteger = 0
    lonely = 0
    for x in range(len(a)):
        for y in range(len(a)):
            if(a[x] == a[y]):
                numInteger += 1
        if(numInteger == 1):
            lonely += a[x]
        numInteger = 0
    
    #print(set(a))
    #print(sum(set(a)))
    #print(a)
    #print(sum(a))
    #print(sum(set(a)) - sum(a))
    #print(sum(a)-sum(set(a)))
    #print(2*sum(set(a)))
    #print(2*sum(set(a)) - sum(a))
    print(lonely)

            


if __name__ == '__main__':

    a = [0,0,1,3,3]

    result = lonelyinteger(a)
