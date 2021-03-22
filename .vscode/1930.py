
n, k = map(int, input().split())

def SuperSum(n, k):
    result = 0
    
    if(k==0):
        return n
    for i in range(1, n+1):
        result += SuperSum(k-1, i)
    return result

while(n, k != EOFError):
    print(SuperSum(n,k))
