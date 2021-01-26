# 1171 당신의 학번은? 2
"""
grade, room, num = map(int, input().split())
if room<10:
    room = '0' + str(room)
    if num<10:
        num = '00' + (str)(num)
    elif num<100:
        num = '0' + (str)(num)
    else:
        num = num

a = str(grade) + room + num
print(a)
"""

# 1172 세 수 정렬하기
"""
number = list(map(int, input().split()))
number.sort()                   // 수를 작은 것부터 나열하기 위해서 파이썬에서는 sort라는 함수를 사용

print(number[0], number[1], number[2])
"""

# 1173 30분전
"""
time, minute = map(int, input().split())

if (minute-30<0):
    time = time - 1
    minute = minute +30
    print(time, minute)
elif (minute-30>0):
    time = time
    minute = minute - 30
    print(time, minute)
elif (minute - 30 == 0):
    time = time
    minute = minute - 30
    print(time, 0+minute)
else:
    print("시간을 확인해 주세요.")
"""

# 1174 30분전 (if는 아직)
"""
hour, minute = map(int, input().split())

hour += 24
minute = minute + hour * 60
minute -= 30
hour = minute / 60
hour = hour % 24
minute = minute % 60

print(int(hour), int(minute))
"""


# 1180 만능 휴지통
"""
a = input()  => String 형태로 받음

b = a[1] + a[0]  => String 형태로 입력받기 때문에 별 다른 함수 없이 자리 바꾸기 가능
b = int(b) * 2

if(b > 99):
    b = b % 100

if(b <= 50):
    print(b)
    print('GOOD')
else:
    print(b)
    print("Oh My God")
"""