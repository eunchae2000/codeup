# 1537 함수로 Hello 또는 World 출력

"""
n = int(input())

def say():
    if n == 1:
        return "Hello"
    elif n == 2:
        return "World"
    else:
        return "확인해주세요"

print(say())
"""

# 1538 함수로 odd 또는 even 출력

"""
n = int(input())

def pr():
    if n%2 == 0:
        return "even"
    else:
        return "odd"

print(pr())
"""

# 1539 함수로 flase 또는 true 출력

"""
n = int(input())

def boolean():
    if n == 0:
        return "false"
    else:
        return "ture"

print(boolean())
"""

# 1540 함수로 zero 또는 non zero 출력

"""
n = int(input())

def zero():
    if n == 0:
        return "zero"
    else:
        return "non zero"

print(zero())
"""

# 1541 함수로 negative/zero/postive 출력

"""
n = int(input())

def pr():
    if n<0:
        return "negative"
    elif n == 0:
        return "zero"
    else:
        return "positive"

print(pr())
"""

# 1542 함수로 prime 또는 composite 출력

"""
n = int(input())

def num():
    for i in range(2, n//2):
        if n%i==0:
            return "composite"
        break
    return "prime"

print(num())
"""

# 1543 함수로 love 출력

"""
n = int(input())

def love():
    for i in range(0, n):
        return "love\n"

print(love()*n)
"""

# 1544 함수로 * n 출력

"""
n = int(input())

def star():
    for i in range(0, n):
        return "*"
print(star()*n)
"""

# 1545 함수로 zero 또는 non zero 출력

"""
n = int(input())

def num():
    if n == 0:
        return "zero"
    else:
        return "non zero"

print(num())
"""

# 1546 함수로 plus/ zero/ minus 판별해서 출력

"""
n = int(input())

def num():
    if n>0:
        return "plus"
    elif n == 0:
        return "zero"
    else:
        return "minus"
print(num())
"""

# 1547 함수로 prime /composite 판별해서 출력

"""
n  = int(input())

def num():
    for i in range(2, n//2):
        if n%i == 0:
            return "composite"
            break
    return "prime"

print(num())
"""

# 1548 함수로 학점 리턴하기

"""
n = int(input())

def score():
    if n>=90 and n<=100:
        return "A"
    elif n>=80 and n<90:
        return "B"
    elif n>=70 and n<80:
        return "C"
    elif n>=60 and n<70:
        return "D"
    elif n>60:
        return "F"
    else:
        return "점수를 확인해 주세요"

print(score())
"""

# 1549 함수로 절대값 리턴

"""
n = int(input())

def num():
    return abs(n)

print(num())
"""

# 1550 함수로 양의 제곱근의 정수 부분만 리턴

"""
import math

n = int(input())

def num():
    if n>0:
        nn = math.sqrt(int(n))
        return int(nn)
    else:
        return 0
    
print(num())
"""