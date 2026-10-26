from functools import cmp_to_key

def find_euclidean_distance(x1, y1, x2, y2):
    return (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) 


def comp(a,b):
    if a[2] != b[2]:
        return a[2] - b[2]
    if a[0] != b[0]:
        return a[0] - b[0]
    return a[1] - b[1]



n, a, b = map(int, input().split())

point = []
for _ in range(n):
    x, y = input().split()
    distance = find_euclidean_distance(a,b,int(x),int(y))
    point.append((int(x), int(y), distance))

point.sort(key=cmp_to_key(comp))

for x, y, distance in point:
    print(x,y)