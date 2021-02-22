def num():
    a, b, c = map(int, input().split())

    if a>=b:
        if b>=c:
            return b
        elif c>=a:
            return a
        else :
            return c
    elif c>=b:
        return b
    elif c<=a:
        return a
    else:
        return c

print(num())