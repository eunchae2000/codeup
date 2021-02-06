# 1361 별 계단 만들기

"""
num = int(input())

for i in range(0, num):
    for j in range(0, i):
        print(" ", end = " ")
    print("**")
"""

# 1362 숫자 피라미드 3

"""
n = int(input())
​
​
def get_max_num(n):
    num = 0
    for i in range(1, n+1):
        num += i
    return num
​
​
number = get_max_num(n)
for i in range(1, n+1):
    for j in range(0, i):
        print(number, end=' ')
        number -= 1
    print()
"""

# 1365 사각형 출력하기 3

"""
n = int(input())
​
for i in range(0, n):
    print("*", end = " ")
print()

for i in range(1, n-1):
    for j in range(0, n):
        if(j==0 or j==1 or j==n-1 or j==n-i-1):
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

for i in range(0, n):
    print("*", end = " ")
print()
"""

# 1366 사각형 출력하기 4

"""
n = int(input())
​
for i in range(0, n):
    print('*', end='')
print()
​
for i in range(1, int(n/2)):
    for j in range(0, n):
        if (j == 0) or (j == i) or (j == int(n/2)) or (j == n-1) or (j == n-i-1):
            print('*', end='')
        else:
            print(' ', end='')
    print()
​
for i in range(0, n):
    print('*', end='')
print()
​
for i in range(int(n/2), 1, -1):
    for j in range(0, n):
        if (j == 0) or (j == i-1) or (j == int(n/2)) or (j == n-1) or (j == n-i):
            print('*', end='')
        else:
            print(' ', end='')
    print()
​
for i in range(0, n):
    print('*', end='')
print()
"""

# 1367 평행사변형 출력하기 1

"""
응용버전 1
n = int(input())

for i in range(0, n):
    for j in range(i, 0, -1):
        print(" ", end = " ")
    for j in range(0, n):
        print("*", end = " ")
    print()

답:
n = int(input())

for i in range(n-1, -1, -1):
    for j in range(0, i):
        print(" ", end = " ")
    for j in range(0, n):
        print("*", end = " ")
    print()
"""

# 1368 평행사변형 출력하기 2

"""

a, b, c = input().split()
a = int(a)
b = int(b)

if(c=='L'):
    for i in range(0, a):
        for j in range(i, 0, -1):
            print(" ", end = " ")
        for j in range(0, b):
            print("*", end = " ")
        print()

else:
    for i in range(a-1, -1, -1):
        for j in range(0, i):
            print(" ", end = " ")
        for j in range(0, b):
            print("*", end = " ")
        print()
"""

# 1369 빗금 친 사각형 출력하기

"""
a, b = map(int, input().split())

for i in range(1, a+1):
    for j in range(1, a+1):
        if(i==1 or i==a or j==1 or j==a):
            print("*", end = " ")
        elif(i+j-1) % b ==0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()
"""

# 1370 지그재그 출력하기

"""
h, r = map(int, input().split())
​
​
def zigzag(h):
    for i in range(0, h):
        for j in range(0, i):
            print(' ', end='')
        print('*')
    for i in range(h-2, -1, -1):
        for j in range(0, i):
            print(' ', end='')
        print('*')
​
​
for i in range(0, r):
    zigzag(h)
"""