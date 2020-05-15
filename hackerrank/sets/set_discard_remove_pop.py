n = int(input())
s = set(map(int, input().split()))
a = int(input())
for x in range(a):
    i = input().split()
    if i[0] == 'pop':
        s.pop()
    elif i[0] == 'remove':
        s.remove(int(i[1]))
    elif i[0] == 'discard':
        s.discard(int(i[1]))
print(sum(s))
