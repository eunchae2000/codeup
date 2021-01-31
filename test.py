# 1161 First Special Judge
"""
a = list(map(int, input().split()))
b = False

for i in a:
    if i % 5 == 0:
        print(i)
        b = True
        break

if b == False:
    print('0')
"""

# 1165 구구단 출력하기1
"""
num = int(input())

for i in range(1, 10):
    print(str(num)+" X "+str(i)+" = "+str(num*i))
"""
# 1166 n개의 수의 합
"""
num = int(input())
n = list(map(int, input().split()))
sum1 = 0

for i in n:
    sum1 += i

print(sum1)
"""
# 1167 n개의 수 중 5의 배수의 합
"""
num = int(input())
n = list(map(int, input().split()))
sum1 = 0

for i in n:
    if i%5==0:
        sum1 += i

print(sum1)
"""
# 1168 n개의 수 중 짝수의 개수 
"""
num = int(input())
n = list(map(int, input().split()))
sum1 = 0

for i in n:
    if i%2==0:
        sum1 += 1
print(sum1)
"""
# 1169 수열의 값 구하기
"""
a, b, c, n = map(int, input().split())
sum1 = a

for i in range(0, n-1):
    sum1 = sum1 * b + c
print(sum1)
"""
# 1170 1의 개수는? 1
"""
n = int(input())
sum1 = 0

for i in range(1, n+1):
    if(i%10 == 1):
        sum1 += 1
print(sum1)
"""