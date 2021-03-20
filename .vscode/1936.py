def LCA(n, m):
    if(n == m):
        return 0
    elif(n>m):
        return LCA(n//2, m)+1
    elif(n<m):
        return LCA(n, m//2)+1

a, b = map(int, input().split())

print(LCA(a, b))