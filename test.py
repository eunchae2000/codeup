# 1121 나머지 구하기

"""
a, b = map(int, input().split())
c = a%b

print(c)
"""

# 1122 초를 분/초로 변환

"""
second = int(input())
a = second/60
b = second%60

print("%.0f %d" %(a, b))
"""

# 1123 섭씨 온도를 화씨 온도로 변환

"""
c = int(input())

h = (9/5)*c+32
print("%.3f" %h)
"""

# 1124 분자량 구하기1

"""
a = input()
key = a.index('H')
num1 = a[1:key]
num2 = a[key+1:]
print(int(num1)*12 + int(num2)*1)
"""

# 1125 8진수 16진수 변환

"""
a = int(input())
print("%o %X" %(a, a))
"""

# 1126 정수 계산기

"""
a, b = map(int, input().split())
c = a+b
d = a-b
e = a*b
f = a/b
g = a%b

print("%d + %d = %d" %(a, b, c))
print("%d - %d = %d" %(a, b, d))
print("%d X %d = %d" %(a, b, e))
print("%d / %d = %d" %(a, b, f))
print("%d '%' %d = %d" %(a, b, g))

or

num1, num2 = input().split()
op = ['+', '-', '*', '/', '%']
for i in range(5): print(num1 + ' ' + op[i] + ' ' + num2 + ' =', int(eval(num1+op[i]+num2)))
"""

# 1127 성적 계산

"""
sum = 0
for i in range(3):
    a, b = input().split()
    sum = sum + (float(a) * int(b))
print(sum)
"""

# 1128 n*123456789

"""
a = int(input())
b = a*123456789

print(b)
"""