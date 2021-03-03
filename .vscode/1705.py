n = str(input())
m = 0

if (int(n)>=100 and int(n)<=999):
    if(int(n[0])==3 or int(n[0])==6 or int(n[0]) == 9):
        m += 1
        if(int(n[1])==3 or int(n[1])==6 or int(n[1]) == 9):
            m += 1
            if(int(n[2])==3 or int(n[2])==6 or int(n[2]) == 9):
                m += 1
        elif(int(n[2])==3 or int(n[2])==6 or int(n[2]) == 9):
            m += 1
    elif(int(n[1])==3 or int(n[1])==6 or int(n[1]) == 9):
        m += 1
        if(int(n[2])==3 or int(n[2])==6 or int(n[2]) == 9):
            m += 1
    elif(int(n[2]) == 3 or int(n[2]) == 6 or int(n[2]) == 9):
        m += 1
    else:
        print(n)
elif(int(n)<100 and int(n)>=10):
    if(int(n[0]) == 3 or int(n[0]) == 6 or int(n[0]) == 9):
        m += 1
        if(int(n[1]) == 3 or int(n[1]) == 6 or int(n[1]) == 9):
            m += 1
    elif(int(n[1]) == 3 or int(n[1]) == 6 or int(n[1]) == 9):
        m += 1
    else:
        print(n)
elif(int(n)<10 and int(n)>=0):
    if(int(n[0]) == 3 or int(n[0]) == 6  or int(n[0]) == 9):
        m += 1
    else:
        print(n)
else:
    print(n)

if(m==3):
    print("KKK")
elif(m==2):
    print("KK")
elif(m==1):
    print("K")