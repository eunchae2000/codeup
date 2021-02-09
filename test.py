# 1411 빠진 카드
"""
n = int(input())
cards = []
miss = []

for i in range(1, n+1):
    cards.append(i)

for i in range(0, n-1):
    num = int(input())
    miss.append(num)

for i in miss:
    cards.remove(i)

print()
print(cards[0])
"""
# 1412 알파벳 개수 출력하기
"""
string = input()
alphabets = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}
​
for i in string:
    if 97 <= ord(i) <= 122:
        alphabets[i] += 1

for i in range(97, 122+1):
    print(chr(i) + ":" + str(alphabets[chr(i)]))
"""

# 1413 말하는 앵무새
"""
string = input()

for i in range(len(string)-1, -1, -1):  # 뒤에서부터 출력되게 하는 것 (반복문, 배열 사용)
    print(string[i], end = "")
"""
# 1414 C언어를 찾아라
"""
stirng = input()
stirng = stirng.upper()
result1 = 0
result2 = 0

for i in range(len(stirng)):
    if(stirng[i] == 'C'):
        result1+=1
        if(i != len(stirng)-1 and stirng[i+1] == 'C'):
            result2+=1

print(result1)
print(result2)
"""   

# 1415 가장 큰 수
"""
num = list(map(int, input().split()))
result1 = 0
result2 = 0

for i in num:
    if(i%2==0 and i>result1):
        result1 = i
    elif(i%2!=0 and i>result2):
        result2 = i

print(result1)
print(result2)
"""
# 1416 2진수 변환
"""
num = int(input())
num = str(bin(num))     # 2진수를 문자열로 변환

print(num[2:])      # 문자열로 변환 후 2진수의 앞에 붙는 ob 뒤부터 출력해야 하기 때문에 [2:] 시작
"""
# 1417 범인을 잡아라 2 10명의 키를 입력하고 3번째로 큰 키를 출력
"""
num = list(map(int, input().split()))
num.sort(reverse=True)      # sort = 기본값은 오름차순으로 정렬
                            # reverse = sort의 옵션으로 true는 내림차순으로 정렬 만약 false라면 그대로 오름차순으로 정렬

print(num[2])
"""
# 1418 t를 찾아라 t의 문자가 문자열의 어느 순서에 있는지 출력
"""
string = input()

for i in range(0, len(string)):
    if(string[i] == 't'):       # 문자열이기 때문에 " "로 검색
        print(i+1, end = " ")
"""
# 1419 love 2 문자열을 입력받고 그 문자열 안에 'love'라는 단어가 몇 개 들어있는지 출력
"""
string = input()
count = 0

for i in range(0, len(string)):
    if(string[i:i+4] == 'love'):
        count += 1

print(count)
"""
# 1420 3등 찾기
"""
n = int(input())
hash_record = {}
​
for i in range(0, n):
    name, score = input().split()
    hash_record[name] = int(score)
​
# sorted => 기존의 리스트를 새로 정렬하여 새로운 리스트를 만드는 것 True -> 내림차순 정렬 False -> 오름차순 정렬 

data = sorted(hash_record.items(), key=lambda t: t[1], reverse=True)
print(data[2][0])
"""