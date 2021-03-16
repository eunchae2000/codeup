# 방법 1
"""
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
"""

# 방법 2
"""
n = int(input())

def star(n):
    if n>0:
        star(n-1)
        print("*"*n)
star(n)
"""