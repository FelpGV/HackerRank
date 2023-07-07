import string
from unittest import result


def matchingStrings(strings, queries):
    n = 0
    result = []
    for x in range(len(queries)):
        for y in range(len(strings)):
            if(queries[x] == strings[y]):
                n += 1
        result.append(n)
        n = 0

    res = []
    for q in queries:
        ans = strings.count(q)
        res.append(ans)
    print(res)
        

    return result

if __name__ == '__main__':
    

    strings = ['aba','baba','aba','xzxb']
    queries = ['aba','xzxb','ab']

    res = matchingStrings(strings, queries)
    print(res)