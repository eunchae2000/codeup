
n = str(input())

for i in range(0, len(n)):
    if (n[i] == ','):
        print(" ", end = "")
    elif (n[i] == ';'):
        print("")
    elif(n[i] == ' '):
        continue
    else:
        print(n[i], end = "")