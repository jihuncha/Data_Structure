import heapq

# 최소힙
def heapsort(iterable):
    h = []
    result = []
    # value 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 추출
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 최대힙
def heapsort(iterable):
    h = []
    result = []
    # value 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 추출
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
