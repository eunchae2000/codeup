# 파이썬으로 기약분수 나타내기

from fractions import Fraction  # 기약분수를 만드는 함수

a, b = map(int, input().split())
aa = Fraction(a, b)

print(aa.numerator, aa.denominator)     # 각각 기약분수의 분자와 분모