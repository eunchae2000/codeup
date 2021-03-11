a = int(input())

def num(n):
    if (n<=1):
        return 1
    return n + num(n-1)

print(num(a))