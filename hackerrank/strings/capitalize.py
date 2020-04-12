
def solve(s):
    return ' '.join([x.capitalize() for x in s.split(" ")])


if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)
