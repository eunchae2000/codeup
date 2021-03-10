# 1526 함수로 문자열 Hello 출력
"""
def say():
    return "hello"
a = say()
print(a)
"""

# 1527 함수로 123 숫자 출력

"""
def num():
    return 123
a = num()
print(a)
"""

# 1528 함수로 * 문자 출력

"""
def s():
    return "*"
a = s()
print(a)
"""

# 1529 함수로 ** 문자 출력

"""
def ss():
    return "**"
a = ss()
print(a)
"""

# 1530 함수로 문자 A 출력

"""
def st():
    return "A"
a = st()
print(a)
"""

# 1531 함수로 정수(int) 1 리턴하기

"""
def num():
    return 1
a = num()
print(a)
"""

# 1532 함수로 정수(long long int) -2147483649 리턴하기

"""
def num():
    return -2147483649
a = num()
print(a)
"""

# 1533 함수로 실수(float) 3.14 리턴하기

"""
def num():
    return float(3.14)
a = num()
print("%f" % a)
"""

# 1534 함수로 실수(double) 3.1415926535897 리턴하기

"""
def num():
    return 3.1415926535897
a = num()
print(a)
"""

# 1535 함수로 가장 큰 값 위치 리턴하기 

"""
def num():
    result = 0
    n = int(input())
    m = list(map(int, input().split()))
    return m.index(max(m))+1
print(num())
"""

# 1336 함수로 가장 작은 값 리턴하기

"""
def num():
    m = int(input())
    n = list(map(int, input().split()))

    return min(n)

print(num())
"""