a, b, c = map(int, input().split())

if(b%2==0):
    for i in range(0, 2):
        print(str(a)+str(b)+str(c), end = " ")
else:
    print(str(a)+str(b)+str(c))