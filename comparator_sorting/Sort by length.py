from functools import cmp_to_key

def comparator(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    else:
        return (a > b) - (a < b)


n = int(input())
arr = [input().strip() for _ in range(n)]

arr.sort(key=cmp_to_key(comparator))

for st in arr:
    print(st)
