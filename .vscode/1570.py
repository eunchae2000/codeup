def num():
    n = int(input())
    nn = list(map(int, input().split()))
    m = int(input())
    result = 0

    for i in range(0, n):
        if m<nn[i]:
            result = nn[i]
            result = nn.index(nn[i])+1
            break
        elif m == nn[i]:
            result = i+1
            break
        else:
            result = n+1
    return result

print(num())