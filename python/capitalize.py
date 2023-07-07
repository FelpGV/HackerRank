def solve(s):
    #s = s.title()
    #print(s)

    # capitalize = []


    # for _ in s.split():
    #     capitalize.append(_.capitalize())

    # return " ".join(capitalize)

    # words = s.split(" ")
    # capitalized_words = [w.capitalize() for w in words]
    # return " ".join(capitalized_words)

    for _ in s.split():
        s = s.replace(_, _.capitalize())
    return(s)

    # capitalize = s.split()
    # for string in capitalize:
    #     l = list(string)
    #     l[0] = l[0].upper()
    #     s = s.replace(string,"".join(l))


    # return s

    

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)

#Input
#felipe gil

#output
#Felipe Gil