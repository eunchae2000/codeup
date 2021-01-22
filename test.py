# 1131 문자 출력하기

"""
a = str(input())

print(a)
"""

# 1132 문자열 출력하기

"""
a = str(input())

print(a)
"""

# 1133 공백이 있는 문자열 입출력

"""
a, b, c = input().split()

print(a, b, c)
"""

# 1135 관계 연산자 1

"""
a, b = map(int, input().split())
if a>b:
    print("1")
else:
    print("0")
"""

# 1136 관계 연산자 2

"""
a, b = map(int, input().split())
if (a==b):
    print("1")
else:
    print("0")
"""

# 1137 관계 연산자 3

"""
a, b = map(int, input().split())
if (a!=b):
    print("1")
else:
    print("0")
"""

# 1138 논리 연산자(NOT)

"""
a = int(input())
if (a==1):
    print("0")
elif (a==0):
    print("1")
else:
    print("0 또는 1만 입력하세요.")
"""

# 1139 논리 연산자(AND)

"""
a, b = map(int, input().split())
if ((a == 1) and (b == 1)):
    print("1")
elif((a == 0) and (b == 1)):
    print("0")
elif((a == 1) and (b == 0)):
    print("0")
elif((a == 0) and (b == 0)):
    print("0")
else:
    print("입력을 확인해 주세요.")
"""

# 1140 논리 연산자(OR)

"""
a, b= map(int, input().split())

if ((a==1) or (b==1)):
    print("1")
elif ((a==0) and (b==0)):
    print("0")
else:
    print("숫자를 확인해 주세요.")
"""