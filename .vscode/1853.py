n = int(input())

def num(a):
    if(a<=1):
        return 1
    return a + num(a-1)

result = num(n)
print(result)