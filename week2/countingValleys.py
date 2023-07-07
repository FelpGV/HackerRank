def countingValleys(path):
    levelStep = 0
    valleys = 0
    for _ in path:
        if _ == 'D':
            if levelStep == 0:
                valleys += 1
            levelStep -= 1
        else: 
            levelStep += 1
    return valleys
            
    

if __name__ == '__main__':
    
    path = 'UDDDUDUU'
    valleys = countingValleys(path)
    print(valleys)
    

    


# 8
# UDDDUDUU