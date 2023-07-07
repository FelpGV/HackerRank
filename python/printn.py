if __name__ == '__main__':
    n = int(input())
    values = []
    for x in range(1,n+1):
        print(x)
        values.append(x)

    print(*values, sep='', end='\n')
    