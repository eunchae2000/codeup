n = int(input())

def num(n):
    if(n<2):
        return n
    else:
        return num(n-1) + num(n-2)
print(num(n))