T = int(input())
for _ in range(T):
    An, A = int(input()), set(input().split())
    Bn, B = int(input()), set(input().split())
    print(A.issubset(B))
    
    