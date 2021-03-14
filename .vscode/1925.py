n, r = map(int, input().split())

def num(n, r):
    if(n==r or r==0):
        return 1
    elif(r==1):
        return n
    return num(n-1, r-1) + num(n-1, r)

print(num(n, r))