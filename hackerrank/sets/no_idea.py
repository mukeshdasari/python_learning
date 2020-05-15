n,m = map(int, input().split())
arr = [*map(int, input().split())]
A = set(map(int, input().split()))
B = set(map(int, input().split()))
happiness = 0
for x in arr:
    if x in A:
        happiness += 1
    if x in B:
        happiness -= 1 
print(happiness)