def print_rangoli(size):
    alphabet = 'abcdefgh'
    n = 1
    for h in range(2*size-1):
        for l in range(4*size-3):
            
            print('*',end="")
        print("")

    
    
if __name__ == '__main__':
    # n = int(input())
    n = 2
    print_rangoli(n)

# import string
# alpha = string.ascii_lowercase

# n = int(input())
# L = []
# for i in range(n):
#     s = "-".join(alpha[i:n])
#     L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#     print(L)
#print('\n'.join(L[:0:-1]+L))