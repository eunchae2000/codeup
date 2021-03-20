def LCA(n, m):
    if(n == m):
        return n
    elif(n>m):
        return LCA(n//2, m)
    elif(n<m):
        return LCA(n, m//2)

a, b = map(int, input().split())

print(LCA(a, b))