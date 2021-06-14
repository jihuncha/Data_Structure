# bisect

* 파이선에서 이진 탐색을 쉽게 탐색할 수 있도록 `정렬된 배열에서 특정 원소를 찾아야할 때` 사용
* bisect_left, bisect_right 는 시간복잡도 O(LogN) 에 동작

### 종류
* bisect_left : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 때 가장 왼쪽 인덱스 반환
* bisect_right : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 때 가장 왼쪽 인덱스 반환

~~~python
from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4

print(bisect_left(a,x))
print(bisect_right(a,x))

# 2
# 4
~~~

### 정렬된 리스트에서 값이 특정 범위에 속하는 원소 구하기
    * 원소의 값을 x라고 할 때 left_value <= x <= right_value인 원소를 O(LogN) 속도로 구하는 방법

~~~python
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a,left_value)
    print("count_by_range/right - ", right_index)
    print("count_by_range/left - ",left_index)

    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

# 값이 4인 데이터 갯수
print(count_by_range(a,4,4))
# 2

print(count_by_range(a,-1,3))
# 6
~~~