n = int(input())

def num(n):
    if(n != 1):
        num(n-1)
    print(n, end = " ")
num(n)