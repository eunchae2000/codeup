# 기초 입출력

#code up 9번   정수 1개 입력받아 그대로 출력

a = 2
print(a)

#code up 10번   문자 1개 입력받아 그대로 출력

b = '아'
print(b)

#code up 11번   실수 1개 입력받아 그대로 출력

c = 3.4
print(c)

#code up 12번   정수 2개를 입력받아 그대로 출력

d = 10
e = 30
print(d, e)

#code up 13번   문자 2개 입력박아 그대로 출력하기

f = '은'
g = '채'

print(f,g)

#code up 14번   실수 입력받아 둘째 자리까지 출력하기

a = float(input())  #python에서 무엇을 입력받기 위해서는 앞에 자료형을 붙이고 input을 적어준다.
print('%.2f' %a)    #%.2 => 소수점 둘째 자리까지 출력한다는 의미리고 %a는 입력받은 a의 숫자로부터 실행한다는 의미

#code up 15번   정수 1개 입력받아 3번 출력하기

h = int(input())
print(h, h, h)

#code up 16번   시간을 입력받아 그대로 출력

i = input()
print(i)

#code up 17번   연월일 입력받아 그대로 출력

year = int(input())
month = int(input())
date = int(input())

print('%04d' %year, ".", '%02d' %month, ".", '%02d' %date)

#code up 18번   주민번호 입력받아 형태 바꿔 출력

code1, code2 = input().split('-')       # 주민번호 앞자리와 뒷자리를 -를 포함해서 입력할 것

print(code1+code2)