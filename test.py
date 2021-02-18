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
