# 1281 홀수는 더하고 짝수는 빼고 3

"""
a, b = map(int, input().split())
sum1 = 0
for i in range(a, b+1):
    if(i%2==0):
        sum1 -= i
        i = '- '+str(i)
        print(i, end = " ")
    else:
        if(a==i):
            sum1 += i
            print(str(i), end = " ")
        else:
            sum1 += i
            i = '+ '+str(i)
            print(i, end = " ")

print("= " + str(sum1))
"""

# 1282 제곱수 만들기

"""
import math
n = int(input())

for i in range(1, n+1):
    t = math.sqrt(n-i)
    if t == round(t, 1):
        print(i, int(t))
        break
"""

# 1283 주식 투자

"""
won = int(input())
day = int(input())
p = list(map(int, input().split()))

result = won
a = " "

for i in p:
    won += won*(i/100)

if(won-result>0):
    a = "good"
elif(won-result == 0):
    a = "same"
else:
    a = "bad"
print("------------")
print(round(won-result))
print(a)
"""

# 1284 암호 해독

"""
num = int(input())
for i in range(1, 10):
    for j in range(1, 10):
        if(i*j==num):
            if(i>j):
                print(j, i)
            elif(i==j):
                print(i, j)
            else:
                print("Wrong Number")
"""

# 1285 계산기 2

"""
expression = input()
result = 0
symbol = ''
lastNumber = 0
lsatSymbol = ''
lastIndex = 0
isFirst = True

for i in range(0, len(expression)):
    if expression[i] in ('+', '-', '*', '/', '='):
        symbol = expression[i]
        number = int(expression[lastIndex:i])
        lastIndex = i+1

        if isFirst:
            isFirst = False
            result += int(number)
            lastNumber = number
            lsatSymbol = symbol
            continue

        if lsatSymbol == '+':
            result += number
            result = int(result)
        elif lsatSymbol == '-':
            result -= number
            result = int(result)
        elif lsatSymbol == '*':
            result *= number
            result = int(result)
        elif lsatSymbol == '/':
            result /= number
            result = int(result)

        lsatSymbol = symbol

print(int(result))
"""

# 1286 최댓값, 최솟값

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

print(max(a, b, c, d, e), min(a, b, c, d, e))
"""

# 1287 구구단을 *로 출력하기

"""
a = int(input())
sum1 = 1
for i in range(1, 10):
    for j in range(0, i*a):
        print("*", end = " ")
    print(" ")
"""

# 1288 nCr(Tiny)

"""
n, c = map(int, input().split())

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n* factorial(n-1)

print(int(factorial(n)/(factorial(c)*factorial(n-c))))
"""

# 1289 가장 큰 운동장

"""
large = 0

for i in range(3):
    a, b = map(int, input().split())
    if(large<a*b):
        large = a*b

print(large)
"""

# 1290 대금 만들기

"""
a = int(input())
result = 0

for i in range(1, a):
    if(a%i==0):
        result += 1

print(result)
"""