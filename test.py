# 1291 바이러스 백신

"""
a, b, c = map(int, input().split())

if (a >= 3000 and b >= 3000 and c >= 3000):
    print("백신의 값을 확인해 주세요.")
else:
    print(min(a, b, c))
"""

# 1292 범인을 잡아라 1

"""
dna = input()
sum1 = 0

for i in range(0,len(dna)):
    sum1 += int(dna[i])

if(sum1%7==4):
    print("suspect")
else:
    print("citizen")
"""

# 1293 1등과 꼴등

"""
num = int(input())
a = list(map(int, input().split(" ")))

print(max(a), min(a))
"""

# 1294 시저의 암호2

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

# 1295 알파벳 대소문자 변환

"""
alphabat = input()
print(alphabat.swapcase())  // 대소문자 바꾸는 함수 = swapcase => (사용) 변수명.swapcase()
"""
# 1296 직사각형의 최대 넓이

"""
n = int(input())
print(int((n/4)**2))
"""

# 1297 단면의 최대 넓이

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

# 1298 Ax + By = C (Large)

"""
a, b, c = map(int, input().split())
result = 0
sum1 = ''
sum2 = ''

for i in range(1, 10):
    for j in range(1, 10):
        result = a*i + b*j

        if(result == c):
            sum1 = i
            sum2 = j
            break
        
        else:
            break
        print("Not Exist")

print(sum1, sum2)
"""

# 1299 Ax + By = C (small)

"""
a, b, c = map(int, input().split())
result = 0
sum1 = ''
sum2 = ''

for i in range(1, 1000):
    for j in range(1, 1000):
        result = a*i + b*j

        if(result == c):
            sum1 = i
            sum2 = j
            break
        
        else:
            break
        print("Not Exist")

print(sum1, sum2)
"""