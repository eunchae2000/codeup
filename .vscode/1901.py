
n = int(input())

def factorial(n):
    if(n < 1):
        return n
    factorial(n-1)
    print(n)

factorial(n)        # return None을 출력 안시키기 위해서는 print 사용 x