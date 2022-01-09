from collections import deque

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

stack.pop()

print(stack)

queue = deque()

queue.append(2)
queue.append(3)
queue.append(4)

print(queue)

queue.popleft()

print(queue)

def recursive_fatorial(n:int):
    if n > 1:
        return recursive_fatorial(n-1) * n
    else:
        return n

print(recursive_fatorial(5))

def iterative_fatorial(n:int):
    start = 1
    for i in range(1, n+1):
        start *= i
    return start

print(iterative_fatorial(5))

def gcd_eculidean(a,b):
    a,b = max(a,b), min(a,b)
    while b != 0:
        a,b = b, a%b
    return a

def lcm(a,b):
    return int(a * b / gcd_eculidean(a,b))

a = 12
b = 20
# 최대 공약수
print(gcd_eculidean(a,b))
# 최소 공배수
print(lcm(a,b))

