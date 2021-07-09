### 내장 함수 (built-in Function)

#### zip 함수
* 동일한 갯수로 이루어진 자료형을 묶어준다.

~~~python
number = [1,2,3,4]
name = ['my', 'name', 'is', 'jihun']

dic = {}
for a,b in zip(number,name):
    print(a,b)
    dic[a] = b

print(dic)

# 1 my
# 2 name
# 3 is
# 4 jihun
# {1: 'my', 2: 'name', 3: 'is', 4: 'jihun'}
~~~

#### map 함수
* 파이썬의 내장 함수인 map()는 여러 개의 데이터를 한 번에 다른 형태로 변환하기 위해서 사용

~~~
map(변환 함수, 순회 가능한 데이터)
~~~

[map_sample](../built_in_function/built_in_map.py)



