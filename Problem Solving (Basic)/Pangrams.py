def pangrams(s):
    return "pangram" if len(set(s.lower())) > 26 else "not pangram"


if __name__ == '__main__':
    s = input()

    result = pangrams(s)

    print(result + '\n')
