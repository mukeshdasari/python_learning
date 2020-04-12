from itertools import combinations
if __name__ == "__main__":
    s, n = input().split()
    for x in range(1, int(n)+1):
        print(*[''.join(c) for c in combinations(sorted(s), int(x))], sep='\n')
