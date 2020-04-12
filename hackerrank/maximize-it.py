from itertools import product
if __name__ == '__main__':
    k, m = map(int, input().split())
    l = [list(map(int, input().split())) for x in range(k)]
    print(max(list(sum([y**2 for y in x]) % m for x in list(product(*l)))))
