def timeConversion(s):
    t = s[-2:]
    h = int(s[:2])
    if t == "PM" and h != 12:
        h += 12
    elif t == "AM" and h == 12:
        h = 0
    return str(h).rjust(2, "0") + s[2:-2]


if __name__ == '__main__':
    s = input()

    result = timeConversion(s)

    print(result + '\n')
