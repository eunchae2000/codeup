# 1492 1차원 누적 합 배열 만들기 5-1
"""
n = int(input())
m = list(map(int, input().split()))
result = 0
i = 0

for i in range(len(m)):
    result += m[i]
    print(result, end = " ")
"""
# 1493 2차원 누적 합 배열 만들기 5-2
"""
n, m = map(int, input().split())
mat=[list(map(int, input().split())) for _ in range(n)]
rix = [[0 for i in range(m+1)] for _ in range(n+1)]
result = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        result += rix[i][j-1] + rix[i-1][j] - rix[i-1][j-1] + mat[i-1][j-1]
        print(result, end = " ")
    print()
"""
"""
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 for i in range(0, M+1)] for _ in range(N+1)]
 
for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + A[i-1][j-1]
 
for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])
"""
# 1494 
# 1495
# 1496
# 1497
# 1498
# 1499
# 1500 2차원 배열에 값 저장하기
"""
n, m = map(int, input().split()) 
result = 0

for i in range(0, n):
    for j in range(0, m):
        result += 1
        print(result, end = " ")
    print()
"""
# 1501 2차원 배열 채우기1
"""
n = int(input())
result = 0

for i in range(0, n):
    for j in range(0, n):
        result += 1
        print(result, end = " ")
    print()
"""
# 1502 2차원 배열 채우기2
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
result = 0

for i in range(0, n):
    for j in range(0, n):
        result += 1
        matrix[i][j] = result

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end = " ")
    print()
"""

# 1503 지그재그 배열 1
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
result = 0

for i in range(0, n):
    if(i%2):
        for j in range(n-1, -1, -1):
            result += 1
            matrix[i][j] = result
    else:
        for j in range(0, n):
            result += 1
            matrix[i][j] = result

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end = " ")
    print()
"""
# 1504 지그재그 배열 2
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
result = 0

for i in range(0, n):
    if (i%2):
        for j in range(n-1, -1, -1):
            result += 1
            matrix[i][j] = result
    else:
        for j in range(0, n):
            result += 1
            matrix[i][j] = result

for i in range(0, n):
    for j in range(0, n):
        print(matrix[j][i], end = " ")
    print()
"""
# 1505 2차원 배열 채우기3 (달팽이)
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
off = 0
col = n
row = n
result = 0

while col > 0 and row > 0:
    for i in range(off, off+col):
        result += 1
        matrix[off][i] = result
    for i in range(off+1, off+row):
        result += 1
        matrix[i][off+col-1] = result
    for i in range(off+col-2, off-1, -1):
        result += 1
        matrix[off+row-1][i] = result
    for i in range(off+row-2, off, -1):
        result += 1
        matrix[i][off] = result
    off += 1
    col -= 2
    row -= 2

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end = " ")
    print()
"""
# 1506 2차원 배열 채우기 4 (역 달팽이 배열)
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
x = n
y = n
result = 0
now = 0

while x>0 and y>0:
  for i in range(now, now+y):
    result += 1
    matrix[i][now] = result
  for i in range(now+1, now+x):
    result += 1
    matrix[now+y-1][i] = result
  for i in range(now+y-2, now-1, -1):
    result += 1
    matrix[i][now+x-1] = result
  for i in range(x+now-2, now, -1):
    result += 1
    matrix[now][i] = result
  now += 1
  y -= 2
  x -= 2

for i in range(0, n):
  for j in range(0, n):
    print(matrix[i][j], end = " ")
  print()
"""
# 1507 4개의 직사각형 넓이
"""
matrix = [[0]*100 for i in range(100)]
result = 0

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            matrix[x][y] = 1

for i in range(0, 100):
    for j in range(0, 100):
        if matrix[i][j] == 1:
            result += 1

print(result)
"""
# 1508 나도 IQ 150
"""
n = int(input())
result = 0
matrix = []

for i in range(1, n+1):
  tmp = [0]*i
  matrix.append(tmp)

for i in range(0, n):
  num = int(input())
  matrix[i][0] = num
  for j in range(1, len(matrix[i])):
    matrix[i][j] = matrix[i][j-1] - matrix[i-1][j-1]

for i in range(0, n):
  for j in range(0, len(matrix[i])):
    print(matrix[i][j], end = " ")
  print()
  """
# 1509 진격 후 결과
"""
matrix = []
problem = False

for i in range(10):
    num = list(map(int, input().split()))
    matrix.append(num)

horse = list(map(int, input().split()))

for i in range(0, 10):
    if (horse[i]==0):
        continue
    problem = False
    for j in range(9, -1, -1):
        if matrix[i][j] != 0:
            if matrix[j][i] > 0:
                print(i+1, end = "crash")
                problem = True
                break
            else:
                print(i+1, "fall")
                problem = True
                break
    if not problem:
        print(i+1, "safe")
"""