# 1476 2차원 배열 빗금 채우기 3-1
# 135
# 246
"""
n, m = map(int, input().split())

for i in range(1, n+1):
    for j in range(0, m):
        print(n*j+i, end = " ")
    print()
"""
# 1477 2차원 배열 빗금 채우기 3-2
# 124
# 356
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(0, m+n-1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1478 2차원 배열 빗금 채우기 3-3
# 421
# 653
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(0, n+m-1):
    for j in range(0,n):
        for k in range(0,m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(0, n):
    for j in range(m-1, -1, -1):
        print(matrix[i][j], end = " ")
    print()
"""
# 1479 2차원 배열 빗금 채우기 3-4 
# 531
# 642
"""
n, m = map(int, input().split())
count = 0
matrix = [[0]*m for i in range(n)]

for i in range(n+m-1, -1, -1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(n-1, -1, -1):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1480 2차원 배열 빗금 채우기 3-5
# 642
# 531
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(n+m-1, -1, -1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1481 2차원 배열 빗금 채우기 3-6
# 653
# 421
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(0, n+m-1):
    for j in range(0,n):
        for k in range(0,m):
            if j+k == i:
                count += 1
                matrix[j][k] = count


for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        print(matrix[i][j], end = " ")
    print()
"""
# 1482 2차원 배열 빗금 채우기 3-7
# 356
# 124
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(0, m+n-1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(n-1, -1, -1):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1483 2차원 배열 빗금 채우기 3-8
# 246
# 135
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(m+n-1, -1, -1):
    for j in range(0, n):
        for k in range(0, m):
            if j+k == i:
                count += 1
                matrix[j][k] = count

for i in range(0, n):
    for j in range(m-1, -1, -1):
        print(matrix[i][j], end = " ")
    print()
"""