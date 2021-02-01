# 1271 최대값 구하기
"""
n = int(input())
num = list(map(int, input().split()))
num_max = 0

for i in num:
    if(i>num_max):
        num_max = i

print(num_max)
"""

# 1272 기부
"""
a, b = map(int, input().split())
result = 0

if(a%2==0):
    result += (a//2*10)
else:
    result += (a//2+1)

if (b%2==0):
    result += (b//2*10)
else:
    result += (b//2+1)

print(result)
"""
# 1273 약수 구하기
"""
n = int(input())
for i in range(1, n+1):
    if(n%i==0):
        print(i, end = " ")
"""
# 1274 소수 판별
"""
n = int(input())
num = []

for i in range(2, n):
    if (n%i==0):
        print("not prime")
        break
    else:
        print("prime")
        break
"""
# 1275 제곱 구하기
"""
n, k = map(int, input().split())
sum1 = 1    # 제곱값으로 증가하기 때문에 시작값이 0이면 안됨

for i in range(k):
    sum1 *= n

print(sum1)
"""
# 1276 팩토리얼 계산
"""
n = int(input())
result = 1

for i in range(1, n+1):
    result *= i

print(result)
"""
# 1277 몇 번째 데이터 출력하기
"""
n = int(input())
a = list(map(int, input().split()))

print(a[0], a[n//2], a[-1])
"""
# 1278 자릿수 계산
"""
n = int(input())

if(n/1 >= 1):
    if(n/10 >= 1):
        if(n/100 >= 1):
            print("3 자릿수")
        else:
            print("2 자릿수")
    else:
        print("1 자릿수")
"""
# 1279 홀수는 더하고 짝수는 빼고 1
"""
a, b = map(int, input().split())
sum1 = 0

for i in range(a, b+1, 1):
    if(i%2==0):
        sum1 -= i
    else:
        sum1 += i

print(sum1) 
"""
# 1280 홀수는 더하고 짝수는 빼고 2
"""
a, b = map(int, input().split())
sum1 = 0
ii = ""

for i in range(a, b+1, 1):
    if(i%2==0):
        sum1 -= i
        ii = ' +'+str(i)
        print(ii, end = "")
    else:
        sum1 += i
        ii = ' -'+str(i)
        print(ii, end = "")

print(' = ' + str(sum1))
"""
