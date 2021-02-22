def num():
    n = int(input())
    nm = list(map(int, input().split()))
    nn = int(input())
    result = 0

    for i in range(0, n):
        if nm[i] == nn:
            result = (i+1)
            break
        else:
            result = -1
    return result

print(num())