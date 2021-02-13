
# 1451 데이터 정렬 (small)

"""
n = int(input())
num = list(map(int, input().split()))
num.sort(reverse=False)

for i in range(n):
    print(num[i])
"""

# 1452 데이터 정렬 (large)

"""
n = int(input())
num = list(map(int, input().split()))
num.sort(reverse=True)

for i in range(n):
    print(num[i])
"""

# 1460 2차원 배열 순서대로 채우기 1-1

"""
n = int(input())
sum1 = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        sum1 += 1
        print(sum1, end = " ")
    print()
"""

# 1461 2차원 배열 순서대로 채우기 1-2

"""
n = int(input())
sum1 = 0

for i in range(0, n):
    for j in range(1, n+1):
        sum1 += 1

for i in range(0, n):
    for j in range(1, n+1):
        print(sum1, end = " ")
        sum1 -= 1
    print()
"""

# 1462 2차원 배열 순서대로 채우기 1-3

"""
n = int(input())

for i in range(1, n+1):
    for j in range(0, n):
        print(n*j+i, end = " ")
    print()
"""

# 1463 2차원 배열 순서대로 채우기 1-4

"""
n = int(input())

for i in range(0, n):
    for j in range(1, n+1):
        print(n*j-i, end = " ")
    print()
"""

# 1464 2차원 배열 순서대로 채우기 1-5

"""
a, b = map(int, input().split())
result = 0

for i in range(b, 0, -1):
    for j in range(a, 0, -1):
        result = i*j
        print(result, end = " ")
    print()
"""

# 1465 2차원 배열 순서대로 채우기 1-6
"""
n, m = map(int, input().split())

for i in range(n-1, -1, -1):
    for j in range(1, m+1):
        print(m*i+j, end = " ")
    print()
"""