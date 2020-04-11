import itertools

if __name__ == '__main__':
    s = input()
    print(*[(len(list(b)), int(a)) for a, b in itertools.groupby(s)])
