from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    letters = input().split()
    k = int(input())

    print("{:.3f}".format(len(
        [*[x for x in combinations(letters, k) if 'a' in x]])/len([*combinations(letters, k)])))
