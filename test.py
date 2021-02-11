# 1425 자리 배치

"""
a, b = map(int, input().split())
students = list(map(int, input().split()))

students.sort()

for i in range(0, int(a/b)+1):
    for j in range(i*b, i*b+b):
        if j>=len(students):
            break
        print(students[j], end = " ")
    print()
"""

# 1430 기억력 테스트 2

"""
a = int(input())
aa =list(map(int, input().split()))
b = int(input())
bb = list(map(int, input().split()))
cc = []

for i in bb:
    for j in aa:
        if(i == j):
            cc[i] == 1
        else:
            cc[i] == 0

for i in cc:
    if(i == 1):
        print("1", end = " ")
    else:
        print("0", end = " ")
"""