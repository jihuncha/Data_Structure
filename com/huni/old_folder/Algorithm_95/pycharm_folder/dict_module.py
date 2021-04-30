# defaultdict 객체
# 존재하지 않는 키를 조회할 경우 에러 대신에 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.

import collections
a = collections.defaultdict(int)

a['A'] = 5
a['B'] = 4

print(a)

# 추가
a['C'] +=1
print(a)

# Counter
# 아이템에 대한 개수를 계산해 딕셔너리로 리턴
a = [1,2,3,4,5,5,5,6,6]
b = collections.Counter(a)
print(b)

#빈도가 높은 아이템 체크 ->
print(b.most_common(2))

# OrderDict 객체 -> linkedhashmap 같은형태인듯
collections.OrderedDict({'banana' : 3, 'apple' : 4, 'pear' : 1, 'orange':2})

# 그러나 파이선 3.7 부터는 딕셔너리 내부 인덱스를 이용하여 입력 순서가 유지되도록 개선됨.