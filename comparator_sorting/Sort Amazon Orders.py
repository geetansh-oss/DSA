from functools import cmp_to_key

def comp(a,b): # 101 1001 5    103 1001 4
    if a[2] != b[2]:
        return b[2] - a[2]
    if a[1] != b[1]:
        return a[1] - b[1]
    
    return (a[0] - b[0])

n = int(input())
order = []

for _ in range(n):
    orderId , timestamp, priority = input().split()
    order.append((int(orderId),int(timestamp), int(priority)))

order.sort(key=cmp_to_key(comp))

for orderId , timestamp, priority in order:
    print(orderId , timestamp, priority)