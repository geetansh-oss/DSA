from functools import cmp_to_key

def comp(a,b):   # 101 1200 LAX     102 1100 JFK
    if a[1] != b[1]:  
        return a[1] - b[1]
    return a[0] - b[0]

n = int(input())
flight = []

for _ in range(n):
    flightNumber, departureTime, destination = input().split()
    flight.append((int(flightNumber), int(departureTime), destination))

flight.sort(key=cmp_to_key(comp))

for flightNumber, departureTime, destination in flight:
    print(flightNumber, departureTime, destination)
