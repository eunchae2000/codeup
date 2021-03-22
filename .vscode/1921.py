"""
n, k = map(int, input().split())
result = 0

def num(n, k):
    if(k == 2):
        result = bin(n)[2:]
        print(result)
    elif(k == 8):
        result = oct(n)[2:]
        print(result)
    elif(k == 16):
        result = hex(n)[2:]
        result = result.upper()
        print(result)
    elif(k == 10):
        result = int(n, k)
        print(result)
num(n, k)
"""

n, k = map(int, input().split())

def num(n, k):
    if(n < 1):
        return
        num(n/k, k)
    if(n % k < 10):
        print("%d" % (n%k))
    elif (n % k >= 10):
        print("%c" % (n%k+55))
num(n, k)
