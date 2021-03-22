n = input()

def num(n):
    if(n == ''):
        return ''
    else:
        return n[-1:] + num(n[:-1])

answer = int(num(n))
print(answer)