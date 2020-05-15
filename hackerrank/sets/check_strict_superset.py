A = set(map(int, input().split()))
n = int(input())
flag = False
for _ in range(n):
    N = set(map(int, input().split()))
    if(A.issuperset(N)):
        flag = True
    else:
        flag = False
        break
print(flag)