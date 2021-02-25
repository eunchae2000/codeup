def num():
  n = int(input())
  result = 0
  sum1 = 0
  re = " "
  if (n>=1000 and n<=9999):
    n1 = int((n/1000)%10)
    n2 = int((n/100)%10)
    n3 = int((n/10)%10)
    n4 = int(n%10)
    result = (n4*1000) + (n3*100) + (n2*10) + (n1*1)
    sum1 = result + n
    if (sum1>=10000 and sum1<=20000):
      a1 = int((sum1/10000)%10)
      a2 = int((sum1/1000)%10)
      a3 = int((sum1/100)%10)
      a4 = int((sum1/10)%10)
      a5 = int(sum1%10)
      if (a1==a5 and a2==a3==a4):
        re = "YES"
      elif (a1==a2==a3==a4==a5):
        re = "YES"
      elif(a1==a5 and a2==a4):
        re = "YES"
      else:
        re = "NO"
    elif (sum1>=1000 and sum1<=9999):
      a1 = int((sum1/1000)%10)
      a2 = int((sum1/100)%10)
      a3 = int((sum1/10)%10)
      a4 = int(sum1%10)
      if (a1==a2==a3==a4):
        re = "YES"
      elif (a1==a4 and a2==a3):
        re = "YES"
      else:
        re = "NO"
  elif (n>=100 and n<=999):
    n1 = int((n/100)%10)
    n2 = int((n/10)%10)
    n3 = int(n%10)
    result = (n3*100) + (n2*10) + (n1*1)
    sum1 = result + n
    if (sum1>=100 and sum1<=2000):
      a1 = int((sum1/100)%10)
      a2 = int((sum1/10)%10)
      a3 = int(sum1%10)
      if (a1==a3):
        re = "YES"
      elif (a1==a2==a3):
        re = "YES"
      else:
        re = "NO"
  elif (n>=10 and n<=99):
    n1 = int((n/10)%10)
    n2 = int(n%10)
    result = (n2*10) + (n1*1)
    sum1 = result + n
    if (sum1>=10 and sum1<=200):
      a1 = int((sum1/10)%10)
      a2 = int(sum1%10)
      if (a1==a2):
        re = "YES"
      else:
        re = "NO"
  else:
    re = "NO"

  return re

print(num())
      