# 1510 홀수 마방진
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
result = 1
x = 0
y = 0

xx = 0
yy = int(n/2)
matrix[xx][yy] = 1

for i in range(2, n*n+1):
    x = xx
    y = yy
    xx -= 1
    yy += 1
    if xx<0:
        xx = n-1
    if yy>n-1:
        yy = 0
    if matrix[xx][yy] == 0:
        matrix[xx][yy] = i
    else:
        xx = x + 1
        yy = y
        matrix[xx][yy] = i

for i in range(0, n):
    for j in range(0, n):
        print(matrix[i][j], end = " ")
    print()
 """

# 1511 테두리의 합
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
sum1 = 0
result = 0

for i in range(0, n):
    for j in range(0, n):
        sum1 += 1
        matrix[i][j] = sum1

for j in range(0, n):
    result += matrix[0][j]
for j in range(1, n):
    result += matrix[j][n-1]
for j in range(n-2, -1, -1):
    result += matrix[n-1][j]
for j in range(n-2, 0, -1):
    result += matrix[j][0]

print(result)
"""
# 1512 숫자 등고선
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
row, col = map(int, input().split())

def abs(nm):
    return nm if nm>0 else -nm
def getnumber(a, b):
    return abs(a-(row-1)) + abs(b-(col-1)) + 1

for i in range(0, n):
    for j in range(0, n):
        print(getnumber(a, b), end = " ")
    print()
"""
# 1513 지그재그 배열 3
"""
n = int(input())
matrix = [[0]*n for i in range(n)]
x = n-1
y = 0
result = 1
a = False

for i in range(n, 0, -1):
  if a == False:
    for j in range(0, i):
      matrix[x][y] = result
      if(j==i-1):
        x += 1
        result += 1
        a = True
      else:
        x -= 1
        y += 1
        result += 1
  else:
    for j in range(0, i):
      matrix[x][y] = result
      if(j==i-1):
        y += 1
        result += 1
        a = False
      else:
        x += 1
        y -= 1
        result += 1
for i in range(0, n):
  for j in range(0, n):
    print(matrix[i][j], end = " ")
  print()
"""
# 1514 레이저 체스
"""
matrix = [[0]*7 for i in range(7)]
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

for i in range(0, 7):
  matrix[3][i] = 1

if x1 == 4:
  for i in range(0, 7):
    matrix[i][y1-1] = 1
  
if x2 == 4:
  for i in range(0, 7):
    matrix[i][y2-1] = 1

if x3 == 4:
  for i in range(0, 7):
    matrix[i][y3-1] = 1

for k in range(2):
  if (matrix[x1-1][y1-1] == 1):
    for kk in range(0, 7):
      matrix[x1-1][kk] = 1
      matrix[kk][y1-1] = 1

  if (matrix[x2-1][y2-1] == 1):
    for kk in range(0, 7):
      matrix[x2-1][kk] = 1
      matrix[kk][y2-1] = 1
      
  if (matrix[x3-1][y3-1] == 1):
    for kk in range(0, 7):
      matrix[x3-1][kk] = 1
      matrix[kk][y3-1] = 1

matrix[x1-1][y1-1] = 2
matrix[x2-1][y2-1] = 2
matrix[x3-1][y3-1] = 2

for i in range(0, 7):
  for j in range(0, 7):
    print(matrix[i][j], end = " ")
  print()
  """