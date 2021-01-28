
# 1226 이번 주 로또

result = list(map(int, input().split()))
me = list(map(int, input().split()))
sum1 = 0
bonus = result[6]

for i in range(0, len(me)):
    if(result[i] == me[i]):
        sum1 = sum1 + 1
if(sum1==6):
    print("1")
elif(sum1==5):
    for i in range(0, len(me)):
        if (bonus == me[i]):
            sum1 = sum1 + 1
        else:
            sum1 = sum1
    if(sum1 == 5):
        print("3")
    elif(sum1 == 6):
        print("2")
elif(sum1==4):
    print("4")
elif(sum1==3):
    print("5")
elif(sum1<=2):
    print("0")
