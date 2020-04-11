def swap_case(s):
    string = []
    for x in range(len(s)):
        if(s[x].isupper()):
            string.append(s[x].lower())
        else:
            string.append(s[x].upper())
    return ''.join(string)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
