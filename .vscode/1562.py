def num():
    n, m = map(int, input().split())
    if n>m: 
        return m
    else:
        return n
        
print(num())