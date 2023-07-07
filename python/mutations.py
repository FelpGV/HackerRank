def mutate_string(string, position, character):
    l = list(string)
    # l[position] = character

    # string = ''.join(l)

    print(string[:5],string[6:])
    string = string[:5] + "k" + string[6:]
    return(string)



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#input
# abracadabra
# 5 k      