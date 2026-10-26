from functools import cmp_to_key

def comparator(a, b):
    if a > b:
        return -1
    elif a < b:
        return 1
    return 0


n = int(input())

arr = list(map(int, input().split()))

arr.sort(key = cmp_to_key(comparator))

print(*arr)
