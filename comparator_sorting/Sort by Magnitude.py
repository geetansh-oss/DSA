from functools import cmp_to_key

def comparator(a, b):
    if (abs(a) != abs(b)):
        return (abs(a) - abs(b))
    else:
        if a < b: return -1
        elif a > b: return 1
        return 0

n = int(input())
arr = list(map(int, input().split()))  # -5 2 -2 3 -3

arr.sort(key=cmp_to_key(comparator))

print(*arr)

