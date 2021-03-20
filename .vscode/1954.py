def star(n):
    if(n>0):
        print("*"*n)
        star(n-1)

n = int(input())

star(n)