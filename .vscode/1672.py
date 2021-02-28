a, b = map(int, input().split())
c = (a//b) + 1
for i in range(1, c):
    if (c>10000):
        if (i>=10000):
            print("번호 초과 오류")
            break
    else:
        print("F-%04d"%i)