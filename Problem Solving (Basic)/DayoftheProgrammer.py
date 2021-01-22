def dayOfProgrammer(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) or (year % 4 == 0 and year < 1918):
        return f"12.09.{year}"
    if year == 1918:
        return f"26.09.{year}"
    return f"13.09.{year}"


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')
