from functools import cmp_to_key

def comp(a,b):
    if a[0] != b[0]:  #  1 2    3 1
        return a[0] - b[0]
    return a[1] - b[1] 

n = int(input())
points = []

for _ in range(n):
    x, y = input().split()
    points.append((int(x), int(y)))

points.sort(key=cmp_to_key(comp))

for x, y in points:
    print(x,y)
