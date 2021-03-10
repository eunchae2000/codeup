n = int(input())

def g(n):
    if(n <= 0):
        return 0
    g(n-1)
    print("*", end = "")

def f(n):
    if(n <= 0):
        return 0
    f(n-1)
    g(n)
    print()
f(n)