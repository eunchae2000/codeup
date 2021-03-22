n = int(input())

def pascal(n):
    arr = [][]
    if(n == 1):
        arr[0] = 1
        print(arr[0])
        return arr
    elif (n == 2):
        arr[0] = 1
        arr[1] = 1
        pascal(n - 1)
    else:
        arr[0] = 1
        arr[n-1] = 1
        temp = [n-1]
        temp = pascal(n-1)

pascal(n)
        