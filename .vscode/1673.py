# 배열 n에서 아무 두 수를 잡고 최대 공약수를 구한 다음 그 최대공약수와 남은 수의 최대공약수를 구함
# 파이썬으로 3개 이상의 최대공약수 구하기

# 만능 디지털 카드키 만들기

n = list(map(int, input().split()))

def num(a, b):          # a, b는 배열 n에서 아무 두 수를 고른 것
    while b != 0 :
        a, b = b, a%b   # a에 b를, b에 a와 b를 나눈 나머지를 교환하여 저장
    return a            # a는 배열 n의 인덱스 0, 1번째의 최대 공약수
 
m = n[0] 
for i in range(len(n)): 
    m = num(m, n[i])  

print(m)