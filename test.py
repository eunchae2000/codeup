# 1081 주사위를 2개 던지면?

"""
a, b = map(int, input().split())

for i in range(1, a+1):
  for j in range(1, b+1):
    print(i, j)
"""

# 1082 16진수 구구단?

"""
print("16진수를 입력하세요.")
a = int(input(), 16)
b = hex(a)[2].upper()

for i in range(1, 16):
  c = hex(a*i)[2:].upper()
  d = hex(i)[2:].upper()
  print(b+" * "+d+" = "+c)
"""

# 1083 3 6 9 게임의 왕이 되자

"""
a = int(input())

for i in range(1, a+1):
  if(i % 3 == 0):
    print("X", end = " ")
  else:
    print(i, end = " ")
"""

# 1084 빛 섞어 색 만들기

"""
a, b, c = map(int, input().split(" "))
count = 0

for i in range(a):
  for j in range(b):
    for k in range(c):
      print(i, j, k)
      count += 1
print(count)
"""

# 1085 소리 파일 저장용량 계산하기

"""
a, b, c, d = map(int, input().split())
aa = (a*b*c*d)/8/1024/1024    => MB 단위로 바꿔주기 위해서 1024 계산

print(round(aa, 1), 'MB')   => round 함수는 반올림 함수로 소수점 첫째자리까지 반올림 한다는 것
"""

# 1086 그림 파일 저장용량 계산하기

"""
a, b, c = map(int, input().split())
x = (a*b*c)/8/1024/1024

print(round(x, 2), 'MB')
"""

# 1087 여기까지! 이제 그만~

"""
a = int(input())
b = 0
for i in range(1, a):
  b += i
  if b>=a:
    break
  else:
    i += i
print(b)
"""

# 1088 3의 배수는 통과?

"""
a = int(input())

for i in range(a+1):
  if i % 3 == 0:
    continue
  else:
    print(i, end=' ')
"""

# 1089 수 나열하기1

"""
a, b, c = map(int, input().split())

for i in range(c+1):
  j = a + (i - 1) * b
print(j)
"""

# 1090 수 나열하기2

"""
a, b, c = map(int, input().split())
for i in range(c+1):
  if b != 0:
    y = a*b**(i-1)
  else:
    y = 0
print(y)
"""