# 1551 함수로 원하는 값의 위치 리턴하기 1

# 내가 푼 풀이
"""
def nm():
    n = int(input())
    num = list(map(int, input().split()))
    nn = int(input())

    for i in num:
        if num[i] == nn:
            return i+1
    return -1

print(nm())
"""

# 정확한 풀이
"""
def f():
	n = int(input())
	my_array = list(map(int, input().split()))
	k = int(input())
	for index, value in enumerate(my_array):        // 리스트가 있는 경우 순서와 리스트의 값을 전달하는 기능
		if value == k:
			return index + 1
	return -1
"""

# 1552 함수로 소수 부분만 리턴
"""
def num():
    n = float(input())
    m = float(n) - int(n)
    return "%.14f"%m
print(num())
"""

# 1553 함수로 정수 올림 한 값 리턴
"""
import math

def num():
    n = float(input())
    m = math.ceil(n)
    return m

print(num())
"""

# 1554 함수로 정수 내림 한 값 리턴
"""
import math

def num():
    n = float(input())
    m = math.floor(n)
    return m

print(num())
"""

# 1555 함수로 n까지의 합 리턴
"""
def plus():
    n = int(input())
    result = 0

    for i in range(1, n+1):
        result += i
    return result

print(plus())
"""

# 1556 함수로 n! 리턴
"""
import math

def num():
    n = int(input())
    result = math.factorial(n)
    return result
print(num())
"""

# 1557 함수로 n의 약수의 개수 리턴
"""
def num():
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if n%i == 0:
            result += 1
    return result
print(num())
"""           

# 1558 함수로 정수 뒤집어 리턴
"""
def num():
    n = int(input())
    temp = ""

    for i in range(len(str(n))):
        if i==0:
            temp += str(n%10)
        elif i>0 and i<len(str(n))-1:
            temp += str(n//(10**i)%10)
        elif i == len(str(n))-1:
            temp += str(n//(10**(len(str(n))-1)))
    return temp
print(num)
"""

# 1559 함수로 두 정수의 합 리턴
"""
def plus():
    n, m = map(int, input().split())
    result = n + m
    return result
print(plus())
"""

# 1560 함수로 두 정수의 차이 값 리턴
"""
def num():
    n, m = map(int, input().split())
    result = 0

    if n>m:
        result = n-m
    else:
        result = m-n
    return result

print(num())
"""