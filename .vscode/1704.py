n = str(input())
a1 = n[0]
a2 = n[1]
a3 = n[7]
age = 0

if(int(n[7]) == 1):
    n1 = str(19)+str(n[0])+str(n[1])
    age = 2012 - int(n1) + 1
    print(age, "M")
elif(int(n[7]) == 2):
    n1 = str(19)+str(n[0])+str(n[1])
    age = 2012 - int(n1) + 1
    print(age, "F")
elif(int(n[7]) == 3):
    n1 = str(20)+str(n[0])+str(n[1])
    age = 2012 - int(n1) + 1
    print(age, "M")
elif(int(n[7]) == 4):
    n1 = str(20)+str(n[0])+str(n[1])
    age = 2012 - int(n1) + 1
    print(age, "F")