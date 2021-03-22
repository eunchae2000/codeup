c = str(input())
x = 0
y = 0
result = 0
"""
for i in range(0, len(c)-3):
    if(c[i] == 'C'):
        if(c[i+1].isalnum):
            if(c[i+2].isalnum):
                if(c[i+3].isalnum):
                    x = str(c[i+1]+c[i+2]+c[i+3])
                    if(c[i])
                x = str(c[i+1]+c[i+2])
            x = str(c[i+1])
    else:
        x = 0

for j in range(0, len(c)-3):
    if(c[j] == 'H'):
        if(c[j+1].isalnum):
            if(c[j+2].isalnum):
                if(c[j+3].isalnum):
                    y = str(c[j+1]+c[j+2]+c[j+3])
                y = str(c[j+1]+c[j+2])
            y = str(c[j+1])
        y = 1
    else:
        y = 0

result = int(x)*12 + int(y)*1
print(result)
"""
s1 = []
s2 = []
n1 = 0
n2 = 0
i = 0

if(c[i] == 'C'):
    i += 1
    while(c[i] != 'H' or c[i] != ' '):
        sn1[i-1] = sn1[i]
        i += 1
    if(i>=2):
        n1 = 