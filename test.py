# 1224 분수 크기 비교

"""
print("분자/분모 순으로 각각 하나씩 입력해 주세요")

a, b, c, d = map(int, input().split())
ab = float(a/b)
cd = float(c/d)

if (ab>cd):
    print(">")
elif (ab == cd):
    print("=")
elif (ab < cd):
    print("<")
else:
    print("분수를 다시 확인해 주세요")
"""

# 1226 이번 주 로또
"""
result = list(map(int, input().split()))
me = list(map(int, input().split()))
sum1 = 0

for i in me:
    if(result[i] == me[i]):
        sum1 = sum1 + 1

if(sum1==6):
    print("1")
elif(sum1==5):
    if (result[6] == me[5]):
        print("2")
    else:
        print("3")
elif(sum1==4):
    print("4")
elif(sum1==3):
    print("5")
elif(sum1<=2):
    print("0")
"""

# 1228 비만도 측정1

"""
cm, weight = map(float, input().split())
result1 =  float(cm-100) * 0.9
result2 =  float((weight-result1) * 100 / result1)

if(result2<=10):
    print("정상")
elif(result2>=10 and result2<=20):
    print("과체중")
elif(result2>20):
    print("비만")
"""

# 1229 비만도 측정2

"""
cm, weight = map(int, input().split())
result = 0
sum1 = 0

if (cm<150):
    result = cm - 150
    sum1 = (weight - result) * 100 / result
elif (cm>=150 and cm<160):
    result = (cm - 150) / 2 + 50
    sum1 = (weight - result) * 100 / result
elif (cm>=160):
    result = (cm - 100) * 0.9
    sum1 = (weight - result) * 100 / result
else:
    print("키와 몸무게를 확인해 주세요")

if (sum1<=10):
    print("정상")
elif(sum1>10 and sum1<=20):
    print("과제중")
else:
    print("비만")
"""

# 1230 터널 통과하기

"""
a, b, c = map(int, input().split())
if (170 < a and 170 < b and 170 < c):
    print("PASS")
elif (170 >= a or 170>= b or 170 >= c):
    print("CRASH", end = " ")
    if (170>=a):
        print(a)
    elif (170>=b):
        print(b)
    elif (170>=c):
        print(c)
    else:
        print( )
else:
    print("터널 높이를 확인해 주세요")
"""

# 1231 계산기1
"""
abc = input()
sum1 = 0
sum2 = 0
result = 0

for i in range(len(abc)):
    if (abc[i] == '+'):
        sum1 = int(abc[:i])
        sum2 = int(abc[i+1:])
        result = sum1 + sum2
    elif (abc[i] == '-'):
        sum1 = int(abc[:i])
        sum2 = int(abc[i+1:])
        result = sum1 - sum2
    elif (abc[i] == 'x'):
        sum1 = int(abc[:i])
        sum2 = int(abc[i+1:])
        result = sum1 * sum2
    elif (abc[i] == '/'):
        sum1 = int(abc[:i])
        sum2 = int(abc[i+1:])
        result = sum1 / sum2

print(result)
"""
