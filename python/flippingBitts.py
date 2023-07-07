from tkinter import N


def flippingBits(n):
    n = str(format(n, "b"))
    listBit = ''
    for _ in range(32-len(n)):
        listBit += '0'
    listBit += n
    n = ''
    for _ in listBit:
        if _ == '0':
            n += '1'
        else:
            n += '0'

    count = 0
    potencial = 0
    for _ in n[::-1]:
        
        count += int(_) * pow(2,potencial)
        potencial += 1

    return count

if __name__ == '__main__':

    n = int(input())


    result = flippingBits(n)
    print(result)
    # q = int(input())

    # for q_itr in range(q):
    #     n = int(input().strip())

    #     result = flippingBits(n)

    #     fptr.write(str(result) + '\n')
