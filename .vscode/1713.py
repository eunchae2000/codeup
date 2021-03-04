a, b = map(int, input().split())
result = 0

for i in range(a, b+1):
    if(i != 12):
        if(i%3 == 0):
          result += i
          if(i%4==0):
            result -= i
        elif(i%4 == 0):
          result -= i
          if(i%3==0):
            result += i
        else:
          result = result
print(result)