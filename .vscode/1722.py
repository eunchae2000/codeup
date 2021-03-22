import math

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
aa = 0
bb = 0
result = 0
result1 = 0
result2 = 0

for i in range(0, n-1):
    for j in range(0, 1):
        aa = (m[i+1][j] - m[i][j])
        bb = (m[i+1][j] - m[i][j])
        result1 += (aa**2)
        result += math.sqrt(result1)
        result2 += (bb**2)
        result += math.sqrt(result2)

print("%.2f" % result)

"""
for j in range(0, n-1):
    x[j] -= x[j+1]
    y[j] -= y[j+1]

    result += math.sqrt((x[j]*x[j]) + y[j]*y[j])
"""