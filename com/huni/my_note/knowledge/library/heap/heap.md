### Heap 자료구조

#### heapq
* 파이선에서 힙 자료구조를 사용하기 위해 heapq 를 사용
* 다양한 알고리즘의 `우선순위 큐 (Priority Queue)` 를 사용하기 위해 구현
* 파이썬의 힙은 최소 힙 (Min Heap) 으로 구성되어 있어, 단순히 원소를 힙에 넣고 뺴는 것 만으로도 오름차순 정렬이 된다.
* 시간 복잡도는 O(NlogN)

#### Heap Sort
* 최소힙 과 최대힙
* 파이선은 최대힙을 지원하지 않는다 -> 음수 사용

~~~python
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
~~~




