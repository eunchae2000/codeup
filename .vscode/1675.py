n = list(input())

for i in range(len(n)):
    if n[i].isupper():
        s[i] = chr((ord(n[i])-ord('A') + -3) % 26 + ord('A'))
    elif n[i].islower():
        n[i] = chr((ord(n[i])-ord('a') + -3) % 26 + ord('a'))
        # chr 함수는 아스크 코드 값을 문자로 반환
        # ord 함수는 문자의 아스키 코드 값을 반환
        # ord 함수는 chr 함수와 반대
print("".join(n))
# "".join(n) 는 리스트에서 문자열로 변환 => 