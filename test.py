
# 1294 시저의 암호2 ★

"""
text = input()
password = ''

for i in range(0, len(text)):
    if text[i] == ' ':
        password += text[i]
    elif ord(text[i]) > 119:
        if text[i] == 'x':
            password += 'a'
        elif text[i] == 'y':
            password += 'b'
        elif text[i] == 'z':
            password += 'c'
    else:
        code = ord(text[i]) + 3
        password += chr(code)
        
print(password)
"""

# 1297 단면의 최대 넓이 ★

"""
n = int(input())
a = 0
b = 0

for i in range(1, int(n/2)):
    if a < i * (n-i * 2):
        a = i * (n-i * 2)
        b = i

print(b)
"""

# 1351 구구단 출력하기2

"""
a, b = map(int, input().split())
result = 1

for i in range(a, b+1):
    for j in range(1, 10):
        result = i*j
        print(str(i) + " X " + str(j) + " = " + str(result))
    print(end = "")
"""

# 1352 사각형 출력하기 1

"""
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end = "")
    print()
"""

# 1353 삼각형 출력하기 1

"""
n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print("*", end = "")
        if(j==i):
            break
        else:
            continue
    print()
"""

# 1354 삼각형 출력하기 2

"""
n = int(input())

for i in range(n+1, 1, -1):
    for j in range(1, i):
        print("*", end = "")
        if(j==i):
            break
        else:
            continue
    print()
"""

# 1355 삼각형 출력하기 3

"""
n = int(input())

for i in range(0, n):
    for j in range(0, i):
        print(" ", end = "")
    for j in range(0, n-i):
        print("*", end = "")
    print()
"""

# 1356 사각형 출력하기 2

"""
n = int(input())

for i in range(1, n+1):
    if(i==1 or i==n):
        for j in range(1, n+1):
            print("*", end = "")
        print()
    else:
        print("*", end = "")
        for j in range(2, n):
            print(" ", end = "")
        print("*", end = "")
        print()
"""

# 1357 삼각형 출력하기 4

"""
n = int(input())
for i in range(1, n+1):
    for j in range(0, i):
        print("*", end = "")
    print()
for i in range(n+1, 1, -1):
    for j in range(1, i-1):
        print("*", end = "")
    print()
"""

# 1358 삼각형 출력하기 5

"""
n = int(input())

for i in range(int(n/2), -1, -1):
    for j in range(0, i):
        print(' ', end='')
    for j in range(0, (n - i * 2)):
        print('*', end='')
    for j in range(0, i):
        print(' ', end='')
    print()
"""

# 1359 숫자 피라미드 1

"""
num = int(input())
n = 1

for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end = "")
        n += 1
    print()
"""

# 1360 숫자 피라미드 2

"""
num = int(input())
n = num

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(i, end = "")
    print()

# 다른 버전
num = int(input())
n = num

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end = "")
    n -= 1
    print()
"""