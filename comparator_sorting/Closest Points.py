from functools import cmp_to_key

def comp(a,b):
    

n, a, b = map(int, input().split())

point = []
for _ in range(n):
    x, y = input().split()
    point.append((int(x), int(y)))

point.sort(key=cmp_to_key(comp))

