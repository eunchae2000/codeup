n = int(input())

def num(n):
    if (n<=1):
        return 1
    return n * (n+1) // 2
result = num(n)
print(result)