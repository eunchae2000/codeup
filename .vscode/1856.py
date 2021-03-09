n = int(input())

def num(a):
    if(a == 0 or a == 1):
        return 1
    elif(a == 2):
        return 2
    elif(a == 3):
        return 4
    else:
        return num(a-1) + num(a-2) + num(a-3)

result = num(n)
print(result)