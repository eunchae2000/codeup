# 1143 비트 연산자 (AND)

"""
a, b = map(int, input().split())
c = a&b

print(c)
"""

# 1144 비트 연산자 (OR)

"""
a, b = map(int, input().split())
c = a|b

print(c)
"""

# 1147 비트 연산자 (<<)

"""
a, b = map(int, input().split())
c = a<<b

print(c)
"""

# 1148 비트 연산자 (>>)

"""
a, b = map(int, input().split())
c = a>>b
print(c)
"""

# 1149 두 수 중 큰 수

"""
a, b = map(int, input().split())
if a>b:
    print(a)
else:
    print(b)
"""

# 1150 세 수 중 가장 작은 수

"""
a, b, c = map(int, input().split())
if a>b:
    if b<c:
        print(b)
    elif c<b:
        print(c)
elif a<b:
    if a<c:
        print(a)
    elif a>c:
        print(c)
"""