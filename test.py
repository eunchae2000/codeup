# 1466 2차원 배열 순서대로 채우기 1-7
"""
n,m = map(int, input().split())

for i in range(0, n):
    for j in range(m, 0, -1):
        print(n*j-i, end = " ")
    print()
"""
# 1467 2차원 배열 순서대로 채우기 1-8
"""
n, m = map(int, input().split())

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        print(n*j-i+1, end = " ")
    print()
"""
# 1468 2차원 배열 지그재그로 채우기 2-1
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
count = 0

for i in range(0, n):
    if i%2:
        for j in range(n-1, -1, -1):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(0, n):
            count += 1
            matrix[i][j] = count

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end = " ")
    print()
            
"""
# 1469 2차원 배열 지그재로 채우기 2-2
"""
n = int(input())

for i in range(1, n+1):
    if i%2:
        for j in range(i*n, i*n-n, -1):
            print(j, end = " ")
    else:
        for j in range(i*n-n+1, i*n+1):
            print(j, end = " ")
    print()
"""
# 1470 2차원 배열 지그재로 채우기 2-3 
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
count = 0

for i in range(0, n):
    if i%2:
        for j in range(n-1, -1, -1):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(0, n):
            count += 1
            matrix[i][j] = count

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end = " ")
    print()
"""
# 1471 2차원 배열 지그재로 채우기 2-4
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
count = 0

for i in range(0, n):
    if i%2:
        for j in range(0, n):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(n-1, -1, -1):
            count += 1
            matrix[i][j] = count

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end = " ")
    print()
"""
# 1472 2차원 배열 지그재로 채우기 2-5
"""
n, m = map(int, input().split())
count = 0
matrix = [[0]*m for i in range(n)]

for i in range(0, n):
    index = n-i-1
    if i%2:
        for j in range(0, m):
            count += 1
            matrix[index][j] = count
    else:
        for j in range(m-1, -1, -1):
            count += 1
            matrix[index][j] = count

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1473 2차원 배열 지그재로 채우기 2-6
"""
n, m = map(int, input().split())
matrix = [[0]*m for i in range(n)]
count = 0

for i in range(0, n):
    index = n-i-1
    if i%2 :
        for j in range(m-1, -1, -1):
            count += 1
            matrix[index][j] = count
    else:
        for j in range(0, m):
            count += 1
            matrix[index][j] = count

for i in range(0, n):
    for j in range(0, m):
        print(matrix[i][j], end = " ")
    print()
"""
# 1474 2차원 배열 지그재로 채우기 2-7
"""
n, m = map(int, input().split())
matrix = [[0]*n for i in range(m)]
count = 0

for i in range(0, m):
    if i%2:
        for j in range(n-1, -1, -1):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(0, n):
            count += 1
            matrix[i][j] = count

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        print(matrix[j][i], end = " ")
    print()
"""
# 1475 2차원 배열 지그재로 채우기 2-8
"""
n, m = map(int, input().split())
count = 0
matrix = [[0]*n for i in range(m)]

for i in range(0, m):
    if i%2:
        for j in range(0, n):
            count += 1
            matrix[i][j] = count
    else:
        for j in range(n-1, -1, -1):
            count += 1
            matrix[i][j] = count

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        print(matrix[j][i], end = " ")
    print()
"""