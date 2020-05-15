na = input()
a = set(map(int, input().split()))
no = int(input())
for i in range(no):
    operation = input().split()[0]
    o = set(map(int,input().split()))
    getattr(a, operation)(o)
print(sum(a))
    