
if __name__ == '__main__':
    n1 = input()
    a = set(map(int, input().split()))
    n2 = input()
    b = set(map(int, input().split()))

    print('\n'.join([str(x) for x in sorted(a ^ b)]))
    # print('\n'.join([str(x) for x in sorted((a.union(b).difference(a.intersection(b)))))))
