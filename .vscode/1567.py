def num():
    n = int(input())
    nn = list(map(int, input().split()))
    m, mm = map(int, input().split())
    result = 0
    for i in range(m-1, mm):
        result += nn[i]
    return result
print(num())