k = int(input())
rooms = input().split()
s, m = set(), set()
for x in rooms:
    if x not in s:
        s.add(x)
    else:
        m.add(x)

print(s.symmetric_difference(m).pop())