n = int(input())

def num(n):
    if (n>0):
        print(n)
        return num(n-1)

num(n)