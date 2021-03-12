n = int(input())

def num(n):
    if(n==1):
        return 1
    elif(n==2):
        return 2
    else:
        return n*num(n-1)
print(num(n))