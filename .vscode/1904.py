a, b = map(int, input().split())

def num(a, b):
    if(a>b):
        return
    if(a%2!=0):
        print(a, end=" ")
    num(a+1, b)
num(a, b)