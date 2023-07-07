def diagonalDifference(arr):
    lr = 0
    rl = 0
    for x in range(len(arr)):
        lr += (arr[x][x])

    a = len(arr)-1
    for x in range(len(arr)):
        rl += (arr[x][a])
        print((arr[x][a]))
        a -= 1

    return(abs(lr-rl))


if __name__ == '__main__':

    n = 3

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)