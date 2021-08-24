## Stack
    * 선입후출 (First In Last Out) 구조
    * 박스 쌓기라고 생각

* Stack Sample
~~~python
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #최하단 원소부터
print(stack[::-1]) #최상단 원소부터

# [5, 2, 3, 1]
# [1, 3, 2, 5]
~~~

## Queue
    * 선입선출 (First In First Out) 구조
    * 대기줄이라고 생각

* Queue Sample

~~~python
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온거 부터
queue.reverse()
print(queue) #나중에 들어온거 부터

# deque([3, 7, 1, 4])
# deque([4, 1, 7, 3])
~~~

## recursive
    * factorial
    * 유클리드 호재법

* Factorial

~~~python
# for문 이용
def factorial_iterative(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i
    return result

# 재귀 이용
def factorial_recursive(n):
    if n <= 1:
        return 1
    
    return n * factorial_iterative(n-1)


print(factorial_iterative(5))   #120
print(factorial_recursive(5))   #120
~~~

# 최소 공배수(LCM) / 최대 공약수(GCD)
    * 최소 공배수는 x와 y의 배수 중에서 최소 = x와 y의 곱에서 x,y의 최대 공약수를 나누어준 것과 같다
    * 최대 공약수는 x와 y에서 x의 약수이면서 y의 약수 중에 최대값

## 유클리드 호제법 (Euclidean Algorithm) 
    * 최대 공약수 구하는 방법
    * 두 수, a와 b중 더 큰 수를 더 작은 수로 나눈다. (a가 더 크다고 가정하자)
    * 이후 구해진 나머지 값으로 b를 나눠준다. (즉 a / b의 나머지 값이 c라고 했을 때, b / c)
    * 이후 구해진 나머지 값으로 c를 나눠준다. (즉 b / c의 나머지 값이 d라고 했을 때, c / d)
    * 이 과정을 나머지 값이 0이 될 때까지 반복해준다. 나머지가 0이 되었다면, 나눠준 값이 곧 최대 공약수이다.

~~~python
def gcd_euclidean(a, b):
  a, b = max(a, b), min(a, b)
  while b != 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return int(a * b / gcd_euclidean(a, b))

a = 12
b = 20
print(gcd_euclidean(a, b))
print(lcm(a, b))
~~~

* math 사용
~~~python
import math

# 최대 공약수
print(math.gcd(12,20))
# 최소 공배수
print(12 * 20 // math.gcd(12,20))
~~~

