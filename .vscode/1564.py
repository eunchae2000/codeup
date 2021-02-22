def num():
    a, b = map(int, input().split())
    while b:
        a, b = b, a%b
    return a

print(num())