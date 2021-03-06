a = str(input())
b = str(input())
call = ""

for i in range(0, len(b)):
    if(a[0] == b[i]):
        call += "0"
    elif(a[1] == b[i]):
        call += "1"
    elif(a[2] == b[i]):
        call += "2"
    elif(a[3] == b[i]):
        call += "3"
    elif(a[4] == b[i]):
        call += "4"
    elif(a[5] == b[i]):
        call += "5"
    elif(a[6] == b[i]):
        call += "6"
    elif(a[7] == b[i]):
        call += "7"
    elif(a[8] == b[i]):
        call += "8"
    elif(a[9] == b[i]):
        call += "9"
    else:
        call += " "


print(call)