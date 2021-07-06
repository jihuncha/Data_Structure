### string 정렬

* sorted : 정렬 이후 결과를 반환해줌
* sort : 정렬 결과를 별도로 리턴하지 않고 덮어씀
* join : list 문자열 결합

~~~python
b = 'zbdaf'
print("".join(sorted(b)))

# abdfz
~~~

* 정렬시에 key를 사용하여 옵션을 지정 가능 

~~~python
a = ['ccc', 'aaaa', 'bb', 'd']
print(sorted(a, key=len))

# ['d', 'bb', 'ccc', 'aaaa']
~~~

### re.sub (정규식)
* re.sub（정규 표현식, 대상 문자열 , 치환 문자）

1. 정규 표현식 - 검색 패턴을 지정
2. 대상 문자열 - 검색 대상이 되는 문자열
3. 치환 문자 - 변경하고 싶은 문자

~~~python
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
 # 정규식 \w 는 단어 문자 // ^ not을 의미 -> 단어문자가 아닌 애들은 공백문자로 치환하라
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()]

print(words)
# ['bob', 'hit', 'a', 'ball', 'the', 'hit', 'ball', 'flew', 'far', 'after', 'it', 'was', 'hit']
~~~



