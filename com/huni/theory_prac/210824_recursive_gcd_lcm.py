# factorial
def factorial_iterator(input:int):
    answer = 1
    for i in range(2,input + 1):
        answer *= i

    return answer

print(factorial_iterator(5))   #120

def factorial_recursice(input:int):
    if input <= 1:
        return 1
    return factorial_recursice(input - 1) * input

print(factorial_recursice(5))

#gcm lcm
# 유클리드
def gcd_eculidean(a:int, b:int):
    a, b = max(a,b), min(a,b)
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a:int,b:int):
    return a * b // gcd_eculidean(a,b)


a = 12
b = 20
print(gcd_eculidean(a, b))  # 4
print(lcm(a,b)) #60

import math
print(math.gcd(a,b))

