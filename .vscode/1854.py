n = int(input())

def num(a):
    if(a>=1):
        return a%10 + num(a//10)
    else:
        return 0 

result = num(n)
print(result)