# 1051 두 정수를 입력받아 b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력

"""
a, b = input().split(" ")
c = int(b>a)

print(c)
"""

# 1052 두 정수를 입력받아 a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력

"""
a, b = input().split()
c = int(a!=b)

print(c)
"""

# 1053 1(참) 또는 0(거짓)이 입력되었을 때 반대로 출력

"""
a = int(input())
print(int(not a))
"""

# 1054 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 참일 때에만 참을 출력

"""
a, b = input().split(" ")
c = int((a==b))
print(c)
"""

# 1055 두 개의 참(1) 또는 거짓(0)이 입력될 때, 하나라도 참이면 참을 출력

"""
a, b = map(int,input().split())
if(bool(a) or bool(b)):
  print("1")
else:
  print("0")
"""

# 1056두 가지의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 다를 때에만 참을 출력

"""
a, b = input().split(" ")
c = int((a!=b))

print(c)
"""

# 1057 두 개의 참(1) 또는 거짓(0)이 입력될 때, 참/거짓이 서로 같을 때에만 참을 출력

"""
a, b = input().split(" ")
c = int(a==b)

print(c)
"""

# 1058 두 개의 참(1) 또는 거짓(0)이 입력될 때, 모두 거짓일 때에만 참이 출력

"""
a, b = map(int,input().split(" "))
if((a==0)and(b==0)):
  print("1")
else:
  print("0")
"""

# 1059 입력된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력

"""
a = int(input())
print(~a)
"""

# 1060 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력

"""
a, b = map(int, input().split(" "))
print(a&b)
"""