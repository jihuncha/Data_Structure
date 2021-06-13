# 최대 공약수
def gcd_euclidean(a, b):
  a, b = max(a, b), min(a, b)
  while b != 0:
    a, b = b, a % b
  return a

# 최소 공배수
def lcm(a, b):
  return int(a * b / gcd_euclidean(a, b))

a = 12
b = 20

print(gcd_euclidean(a, b))
print(lcm(a, b))

import math

# 최대 공약수
print(math.gcd(12,20))
# 최소 공배수
print(12 * 20 // math.gcd(12,20))
