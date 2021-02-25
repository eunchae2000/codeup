def num():
    a, b, c = map(int, input().split())
    result1 = max(a, b, c)
    result2 = min(a, b, c)
    result3 = 0
    if (a != result1 and a!= result2):
        result3 = a
    elif (b != result1 and b!=result2):
        result3 = b
    elif (c!= result1 and c!=result2):
        result3 = c
    return str(result2) + " " + str(result3) + " " + str(result1)

print(num())
