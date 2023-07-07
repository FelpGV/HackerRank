def sockMerchant(ar):
    result = 0
    for i in ar:
        for j in ar:
            if i == j:
                result += 1
    print(result)
                
                
        
        
    

if __name__ == '__main__':

    ar = []
    for _ in range(9):
        ar.append(int(input()))

    sockMerchant(ar)

# 10
# 20
# 20
# 10
# 10
# 30
# 50
# 10
# 20

