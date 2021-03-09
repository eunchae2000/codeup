n, r = map(int, input().split())

def num(n, r):
    if(r == 1):
        return n
    elif(n == r):
        return 1
    elif(n<r):
        return 0
    else:
        return num(n-1, r-1) + num(n-1, r)
print(num(n, r))