# codeup 문제 1041~1050 풀이

#codeup 1041 문자 1개를 입력받아 다음 문자 출력
"""
a = input()
a_1 = ord(a)

print(chr(a_1+1))
"""

# 1042 정수 2개 입력받아 나눈 몫 값 출력
"""
a, b = input().split(" ")

x = int(a)
y = int(b)

print("%d" %(x/y))
"""

# 1043 정수 2개 입력받아 나눈 나머지 값 출력
"""
a,b = input().split(" ")
x = int(a)
y = int(b)

print("%d" %(x%y))
"""
# 1044 정수 1개 입력받아 1을 더한 값 출력
"""
a = input()
b = int(a)

print("%d" %(b+1))
"""
# 1045 정수 2개를 입력받아 합, 차, 곱, 나누기 몫, 나누기 나머지, 나누기 소수점 둘째자리 출력
"""
a,b = input().split(" ")
x = int(a)
y = int(b)

print("%d" %(x+y))
print("%d" %(x-y))
print("%d" %(x*y))
print("%d" %(x/y))
print("%d" %(x%y))
print("%.2f" %(x/y))
"""
# 1046 정수 3개를 입력받아 합과 평균 출력
"""
a,b,c = input().split(" ")
x = int(a)
y = int(b)
z = int(c)

print("%d" %(x+y+z))
print("%.1f" %((x+y+z)/3))
"""
# 1047 정수 1개 입력받아 2배의 값 출력
"""
a = input()
b = int(a)

print("%d" %(b*2))
  """
# 1048 정수 2개 입력받아 2의 거듭제곱 값 출력
"""
a = input()
b = input()

x = int(a)
y = int(b)

print("%d" %(x<<y))
"""
# 1049 정수 2개 입력받아 크기 비교 => a가 b보다 크면 1을 출력
"""
a,b = input().split(" ")
x = int(a)
y = int(b)
z = int(a>b)

print(z)
"""
# 1050 정수 2개 입력받아 같으면 1 출력, 같지 않으면 0 출력
"""
a, b = input().split(" ")
x = int(a)
y = int(b)
z = int(a==b)

print(z)
"""