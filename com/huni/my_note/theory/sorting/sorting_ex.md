### 정렬 (Sorting)
    * 데이터를 특정 기준에 따라서 나열하는 것
    * 정렬 알고리즘은 이진 탐색의 전처리 과정!

### 정렬의 종류
* 선택 정렬 (Selection Sort)
  - 데이터가 여러 개 무작위로 있을 때
  - 가장 작은 데이터를 선택해서 맨 앞에 있는 데이터와 바꿈
  - 그 다음 작은 데이터를 앞에서 두 번째데이터와 바꿈
  - 반복
  - 시간 복잡도
    - n + n-1 + n-2 + ... + 2
    - (n제곱 + n)/2 - 1 하면 됨 -> n제곱 + n - 2 / 2
    - O(n제곱) 으로 표현
    
~~~python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)    #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~

<hr>

* 삽입 정렬 (Insertion Sort)
    - 데이터를 하나 씩 확인하면서 각 데이터를 적절한 위치에 삽입
    - 필요할 때만 위치를 바꾸므로, `데이터가 거의 정렬되어 있을때 효율적` 이다
    - 특징
        - 정렬이 이루어진 원소는 항상 오름차순을 유지하고 있다.
        - 삽입한 데이터를 찾을때 왼쪽을 한 칸씩 이동한다고 가정하는 경우, `삽입할 데이터보다 작은 데이터`를 만나면 그 위치에서 멈추면 된다!
    - 시간 복잡도
        - O(n제곱) 이지만 최선의 경우 O(n) 이 된다.
        - 정렬이 거의 되있는 경우는 퀵 정렬보다 강력하다.
    

~~~python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 삽입 정렬 예시
for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스 i 부터 0까지 감소하면서 탐색
        if array[j] < array[j - 1]: #한 칸 씩 왼쪽으로
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 자기보다 작은 데이터를 만나면 그 자리에서 멈춘다.
            break

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~    

<hr>

* 퀵 정렬 (Quick Sort)
    - `병합 정렬` 과 함께, 대부분의 프로그래밍 언어의 정렬에 근간이 되는 알고리즘
    - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 변경
    - `피벗` 이 사용 -> 큰 수와 작은 수를 교환하기 위한 `기준`
    - 피벗을 설정하고 리스트를 분할하는 방식에 따라 퀵 정렬도 분류된다.
        - 책에서는 대표적인 `호어 분할 (Hoare Partition)` 을 설명
        - 리스트에서 첫 번째 데이터를 피벗으로 설정하는 방식
    - 방식
        1. 왼쪽부터는 피벗보다 큰 데이터를 선택, 오른쪽부터는 피벗보다 작은 데이터를 선택하여 두 데이터의 위치를 변경한다
        2. 만약 왼쪽에서 큰 데이터와 오른쪽에서 작은 데이터의 위치가 엇갈릴경우(index) `작은 데이터` 와 `피벗` 의 위치를 변경한다.
        3. 이 경우 피벗보다 왼쪽은 `피벗보다 작은 데이터`, 오른쪽은 `피벗보다 큰 데이터` 가 된다.
        4. 왼쪽과 오른쪽으로 나누어서 동일한 작업을 반복한다. (재귀)
    - 시간 복잡도
        - 최소 O(nlogn)을 보장 (Computer Science 에서 log의 밑은 보통 2이다)
        - 최악의 경우 O(n의제곱)
    
    
    
* original quick sort
~~~python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: #원소가 한 개인 경우 종료
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left+=1
        # 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) -1)
print(array) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~

* python style quick sort
~~~python
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 1개 이하일 경우 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] #작은 애들은 왼쪽
    right_side = [x for x in tail if x > pivot] #큰 애들은 오른쪽
    # print("left - ", left_side)
    # print("right -", right_side)
    # print("pivot - ", pivot)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
~~~
    
<hr>

* 계수 정렬 (Count Sort)
    - 특정한 조건이 부합할 때만 사용할 수 있음. 매우 빠르다.
    - 데이터의 개수가 N 이고 데이터의 최대값이 K일 때 `수행시간 O(N+K)`를 보장한다.
    - 다만 `데이터의 크기 범위가 제한되어 정수 형태로 표현가능한 크기 일 경우` 만 사용 가능 - 100만 넘지 않는 경우
    - 큰 데이터와 작은 데이터의 크기 차이가 너무 클 경우도 사용 불가 - 모든 범위를 담을 list를 선언해야하기 때문
    - 시간 복잡도
        - 수행시간 O(N+K) -> 조건이 제한적

~~~python
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] +=1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ') # 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9
~~~

<hr>

* 정렬 라이브러리
    - 시간 복잡도 O(NlogN) 을 보장
    - 코테에서의 문제
        1. 정렬 라이브러리로 풀 수 있는 문제
        2. 정렬 알고리즘의 원리를 물어보는 문제
        3. 더 빠른 정렬이 필요한 문제 - 계수 정렬 등을 이용해야한다!!
    
