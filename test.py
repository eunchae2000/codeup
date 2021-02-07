# 1371 마름모 출력하기

"""
n = int(input())
​
for i in range(0, n):
    for j in range(n-i-1, 0, -1):
        print(' ', end='')
    print('*', end='')
    for j in range(0, i*2):
        print(' ', end='')
    print('*')
​
for i in range(0, n):
    for j in range(0, i):
        print(' ', end='')
    print('*', end='')
    for j in range((n-i-1)*2, 0, -1):
        print(' ', end='')
    print('*')
"""

# 1373 좌표 이동
# 1378 수열의 합

"""
n = int(input())
result = 0
addNumber = 0
​
for i in range(1, n+1):
    addNumber += i
    result += addNumber
​
print(result)
"""

# 1380 두 주사위의 합

"""
num = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if(num==i+j)
        print(i, j)
"""