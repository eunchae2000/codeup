n = int(input())
print(1)
def num(n):
    if(n%2==0):
        num(n/2)
    else:
        if(n==1):
            return
        else:
            num(n*3+1)
    print(int(n))
num(n)