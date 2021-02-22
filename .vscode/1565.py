"""
def num():
    n, m = map(int, input().split())
    nm = 0
    result = 0
    if n>m:
        nm = n
    else:
        nm = m
    for i in range(nm, (n*m)+1):
        if i%n == 0 and i%m == 0:
            result = i
            break
    return result
print(num())
"""

from math import gcd

def num():
    n, m = map(int, input().split())
    return n*m // gcd(n, m)
print(num())