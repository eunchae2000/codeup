n = int(input())
m = [input().split() for _ in range(n)]
result = 0

for i in range(0, n):
    for j in range(0, 3):
        if(int(m[i][j]) < result):
            result = int(m[i][j])
            if(result < int(m[i][3])):
                print(i+1, result)
                exit()
            else:
                continue
        else:
            result = int(m[i][j])
            if(result < int(m[i][3])):
                print(i+1, result)
                exit()

if(result == 0):
    print("-1")