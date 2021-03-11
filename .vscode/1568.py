def num():
    n = int(input())
    nm = list(map(int, input().split()))
    a, b = map(int, input().split())
    result = nm[a]
    s = 0

    for i in range(a-1, b):
        if result < int(nm[i]):
            result = int(nm[i])
            s = i+1
        else:
            result = int(nm[i])
            if(result == int(nm[i])):
                s = i
            else:
                s = i
    return s

print(num())