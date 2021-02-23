def num():
    n = int(input())
    m = list(map(int, input().split()))
    k = int(input())
    result = 0
    
    for i in range(0, n):
        if m[i]>k:
          result = i+1
          break
        elif m[i] == k:
          result = n+1
        else:
          result = n+1
    return result

print(num())