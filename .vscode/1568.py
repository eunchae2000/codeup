def num():
    n = int(input())
    nm = list(map(int, input().split()))
    a, b = map(int, input().split())
    result = 0

    for i in range(a-1, b):
        if result < nm[i]:
            result = nm[i]
            result = i+1
            break
        else:
            result = nm[i]
            result = i
    return result

print(num())