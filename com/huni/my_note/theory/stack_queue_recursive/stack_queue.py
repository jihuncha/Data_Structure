from collections import deque

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
