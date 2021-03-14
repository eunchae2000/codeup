# 메모이제이션(memoization) 사용  =  이전에 계산한 값을 메모리에 저장
# 컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술이다. 
# 동적 계획법(DP)의 핵심이 되는 기술이라 할 수 있다.

arr = {1:1, 2:1}       # 메모이제이션 사용
n = int(input())

def num(n):
    if n in arr:
        return arr[n]x
    arr[n] = (num(n-1) + num(n-2)) %10009

    return arr[n]

print(num(n))