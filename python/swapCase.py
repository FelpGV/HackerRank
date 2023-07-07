from curses.ascii import islower


def swap_case(s):
    swapCaseWord = ''
    for _ in s:
        if _.islower():
            swapCaseWord += _.upper()
        else:
            swapCaseWord += _.lower()
         
    return swapCaseWord

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)