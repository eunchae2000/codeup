# 1251 1부터 100까지 출력하기

"""
for i in range(1, 101):
    print(i)
"""

# 1252 1부터 n까지 출력하기

"""
n = int(input())
for i in range(1, n+1):
    print(i)
"""

# 1253 a부터 b까지 출력하기

"""
a, b = map(int, input().split())

if (a<b):
    for i in range(a, b+1):
        print(i)
else:
    print("수를 확인해 주세요")
"""

# 1254 알파벳 출력하기

"""

a, b = map(ord, input().split())

if a<b:
    for i in range(a, b+1):
        print(chr(i))
"""

# 1255 두 실수 사이 출력하기
"""
a, b = map(float, input().split())

if (a<b):
    for i in range(a, b, 0.01):
        print("%.2f" %i)
"""

# 1256 별 출력하기

"""
n = int(input())
for i in range(n):
    print("*", end = "")
"""

# 1257 두 수 사이의 홀수 출력하기

"""
a, b = map(int, input().split())
for i in range(a, b+1):
    if (i%2!=0):
        print(i, end = " ")
 """

# 1258 1부터 n까지 합 구하기

"""
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i
    
print(sum)
"""

# 1259 1부터 n가지 중 짝수의 합 구하기

"""
n = int(input())
sum1 = 0
for i in range(1, n+1):
    if i%2==0:
        sum1 += i

print(sum1)
"""

# 1260 3의 배수의 합

"""
a, b = map(int, input().split())
summ = 0
for i in range(a, b+1):
    if (i%3==0):
        summ += i

print(summ)
"""