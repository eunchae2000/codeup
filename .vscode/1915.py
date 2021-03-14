n = int(input())

def num(n):
    if(n<=1):
        return n
    return num(n-1) + num(n-2)
print(num(n))