n = str(input())
result = 0

for i in range(len(n)):
  result += int(n[i])
  if(result<10):
    result = result
  else:
    for i in range(len(n)):
      n1 = int(result / 10)
      n2 = int(result % 10)
      result = n1+n2
print(result)