n = int(input())

def sam(n):
    arr = []
    if(n == 1):
        arr[0] = 1
        print(arr[0])
        return arr
    elif (n == 2):
        arr[0] = 1
        arr[1] = 1
        pascal(n - 1)
    else:
        