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

