n = int(input())
result = 0
print(n)
def num(n):
    result = 0
    if n%2 == 0:
        n = n/2
        print(int(n))
        if (n != 1):
            return num(n)
    else:
        if (n==1):
            return
        else:
            n = 3*n+1
            print(int(n))
            if (n != 1):
                return num(n)
num(n)