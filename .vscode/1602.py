def num():
    # eval 함수는 실행 가능한 문자열을 매개변수로 입력받아 문자열 자체를 실행한 결과값을 리턴
    n = eval(input())
    if n - int(n) == 0:
        n = int(n)
        n = abs(n)
    else:
        n = float(n)
        n = abs(n)
    return n
print(num())