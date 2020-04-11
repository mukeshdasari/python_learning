if __name__ == "__main__":
    n = int(input())
    s = set()
    for x in range(n):
        i = input()
        s.add(i.lower())
    print(len(s))
