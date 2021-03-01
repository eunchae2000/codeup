n = [list(map(int, input().split())) for _ in range(5)]
result = 0
m = 0

for i in range(0, 5):
    for j in range(0, 5):
        result = 0
        for k in range(i-1, i+2):
            if (k<0 or k>4):
                continue
            for y in range(j-1, j+2):
                if (y<0 or y>4):
                    continue
                result += n[k][y]
        if (result>m):
            m = result
print(m)