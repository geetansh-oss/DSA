from functools import cmp_to_key

def comparator(a,b):
    if abs(a) % 10 != abs(b) % 10:
        return abs(a) % 10 - abs(b) % 10
    else:
        return a - b

n = int(input())
arr = list(map(int, input().split()))

arr.sort(key=cmp_to_key(comparator))

print(*arr)