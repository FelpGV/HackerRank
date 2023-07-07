
def gradingStudents(grade):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            up = int(grade/5 + 1) * 5
            if up-grade <= 2:
                result.append(up)
            else:
                result.append(grade)
    return result


if __name__ == '__main__':

    grades = []

    for _ in range(4):
        grade = int(input())
        grades.append(grade)

    
    result = gradingStudents(grades)
    print(result)

#input
#Numbers between 0 and 100