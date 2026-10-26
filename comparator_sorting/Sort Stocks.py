from functools import cmp_to_key

def comp(a,b): # AAPL 150 2000   GOOG 100 1800
    if a[1] != b[1]:
        return a[1] - b[1]
    if a[2] != b[2]:
        return b[2] - a[2]
    
    return (a[0] > b[0]) - (a[0] < b[0])

n = int(input())
stock = []

for _ in range(n):
    name , price, cap = input().split()
    stock.append((name,int(price), int(cap)))

stock.sort(key=cmp_to_key(comp))

for name, price, cap in stock:
    print(name, price, cap)