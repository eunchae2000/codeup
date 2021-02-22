def num():
    n, m = map(int, input().split())
    if n>m: 
        return n
    else:
        return m

print(num())