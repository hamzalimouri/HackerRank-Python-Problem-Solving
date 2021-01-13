def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            grade += 5 - grade % 5
        res.append(grade)
    return res


if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))
