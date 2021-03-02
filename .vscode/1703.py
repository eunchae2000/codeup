n = int(input())
n1 = 3600
n2 = 60
a1 = 0
a2 = 0
a3 = 0

if (n>=3600):
    a1 = int(n/3600)
    a2 = int((n%3600)/60)
    a3 = int(n%60)
    print(a1, a2, a3)
elif(n>=60 and n<3600):
    a2 = int(n/60)
    a3 = int(n%60)
    print(a1, a2, a3)
else:
    a3 = int(n)
    print(a1, a2, a3)
