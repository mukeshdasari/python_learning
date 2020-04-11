from itertools import permutations
if __name__ == "__main__":
    s, k = input().split()
    print(*["".join(x) for x in permutations(sorted(s), int(k))], sep="\n")
