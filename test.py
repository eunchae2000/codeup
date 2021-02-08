# 1382 구구단 출력 (2-5단)

"""
for i in range(1, 10):
    for j in range(2, 6):
        print(str(j) + "X" + str(i) + "=" + str(i*j), end = "")
        print("\t", end = "")
    print()
"""

# 1402 거꾸로 출력하기 3

"""
n = int(input())
num = list(map(int, input().split()))
num.reverse()

for number in num:
    print(number, end = " ")
"""

# 1403 배열 두번 출력하기

"""
n = int(input())
num = list(map(int, input().split()))

for i in num*n:
    print(i)
"""

# 1405 숫자 로테이션
"""
import collections                  # collections 모듈 => 데이터를 처리하기에 유용한 모듈

n = int(input())
num = list(map(int, input().split()))
print("------------------")
num = collections.deque(num)        # collections.deque는 안에 들어가 있는 원소를 양방향으로 삭제와 삽입
num.rotate(1)                       # rotate는 num에 들어있는 원소들은 값(1)만큼 회전시켜주는 것
                                      값이 음수이면 왼쪽으로 회전하고 값이 양수이면 오른쪽으로 회전

for i in range(0, n):
    num.rotate(-1)
    for j in num:
        print(j, end = " ")
    print()
"""

# 1406 love

"""
char = str(input())

if(char == "love"):
    print("I love you")
else:
    print("문자를 다시 확인해 주세요.")
"""

# 1407 문자열 출력하기 1

"""
import re           # re모듈은 특정한 패턴과 일치하는 문자열을 '검색', '치환', '제거' 하는 기능을 지원
                    # 문자열 앞에 r이 붙으면 해당 문자열이 구성된 그대로 문자열로 반환
string = input()
print(re.sub(r'\s+', '', string))       # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
                                        # re.sub => 특정 문자열을 찾은 뒤 다른 문자열로 바꿔주는 방법
"""

# 1408 암호처리

"""
password = input()

str1 = ''
str2 = ''

for i in range(0, len(password)):
    asc = ord(password[i]) + 2          # ord는 아스키코드 값으로 변환
    str1 += chr(asc)
    asc = int((ord(password[i])*7)%80+48)
    str2 += chr(asc)
print("    ")
print(str1)
print(str2)
"""


# 1409 기억력 테스트 1

"""
num = list(map(int, input().split()))
n = int(input())

print(num[n-1])
"""

# 1410 올바른 괄호1(괄호 개수 세기)

"""
string = input()
result1 = 0
result2 = 0

for i in range(len(string)):
    if(string[i] == "("):
        result1 += 1
    elif(string[i] == ")"):
        result2 += 1

print(result1, result2)
"""