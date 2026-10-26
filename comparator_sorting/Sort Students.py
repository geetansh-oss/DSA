from functools import cmp_to_key

def comp(a,b): # a = alice 90 b = bob 95 a < b = 0 a > b = 1
    if a[1] != b[1]:
        return b[1] - a[1]
    
    return (a[0] > b[0]) - (a[0] < b[0])

n = int(input())
student = []

for _ in range(n):
    name , marks = input().split()
    student.append((name,int(marks)))

student.sort(key=cmp_to_key(comp))

for name, marks in student:
    print(name, marks)