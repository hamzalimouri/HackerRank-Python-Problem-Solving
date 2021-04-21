def timeInWords(h, m):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
               "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine"]
    if m <= 30:
        if m == 0:
            return f"{numbers[h]} o' clock"
        elif m == 15:
            return f"quarter past {numbers[h]}"
        elif m == 30:
            return f"half past {numbers[h]}"
        elif m == 1:
            return f"{numbers[m]} minute past {numbers[h]}"
        else:
            return f"{numbers[m]} minutes past {numbers[h]}"
    else:
        if m == 45:
            return f"quarter to {numbers[h + 1]}"
        else:
            return f"{numbers[60 - m]} minutes to {numbers[h + 1]}"


if __name__ == '__main__':
    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result + '\n')
