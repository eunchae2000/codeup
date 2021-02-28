n = int(input())
s = [input() for _ in range(n)]
a = 'xocure'
b = '\t'
result = 0
 
for i in range(0, n):
    if (len(s[i]) <= 3) or ("tap" in s[i]) or ("xocure" in s[i]):
        result += 1
        print(s[i])
    else:
        result += 0

if (result >= 0 and result <= 3):
    print("safe")
elif (result >= 4 and result <= 6):
    print("warning")
elif (result >= 7):
    print("danger")