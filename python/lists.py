if __name__ == '__main__':
    N = int(input())
    listInput = []
    listOutput = []

    for _ in range(N):
        command = input().split()
        listInput.append(command)
    
    for _ in range(len(listInput)):
        if(listInput[_][0] == 'insert'):
            pos = int(listInput[_][1])
            num = int(listInput[_][2])
            listOutput.insert(pos,num)
        elif(listInput[_][0] == 'append'):
            listOutput.append(int(listInput[_][1]))
        elif(listInput[_][0] == 'remove'):
            listOutput.remove(int(listInput[_][1]))
        elif(listInput[_][0] == 'pop'):
            listOutput.pop()
        elif(listInput[_][0] == 'sort'):
            listOutput.sort()
        elif(listInput[_][0] == 'reverse'):
            #listOutput.sort(reverse=True)
            listOutput = listOutput[::-1]
        elif(listInput[_][0] == "print"):
            print(listOutput)


# 4
# insert 0 1
# insert 0 3
# insert 1 2
# print

# 29
# append 1
# append 6
# append 10
# append 8
# append 9
# append 2
# append 12
# append 7
# append 3
# append 5
# insert 8 66
# insert 1 30
# insert 6 75
# insert 4 44
# insert 9 67
# insert 2 44
# insert 9 21
# insert 8 87
# insert 1 75
# insert 1 48
# print
# reverse
# print
# sort
# print
# append 2
# append 5
# remove 2
# print
