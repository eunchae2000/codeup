n = int(input())

def num(n):
    result = 0
    if(n % 2 == 0):
        result += 1
        num(n/2)

    elif(n == 1):
        result += 1

    else:
        if(n != 1):
            result += 1
            num(n*3+1)
    print(result)