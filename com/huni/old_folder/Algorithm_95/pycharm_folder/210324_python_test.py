a = 10
b = a

print(id(10), id(a), id(b))

#b 에 7 을 할당 -> a는 변하지 않는다
#b가 다른 주소값을 보게됨.
b = 7

print(id(10), id(a), id(b))

#is -> 주소값 비교
# == -> 값 비교

a = [1,2,3]
print(a == a)
print(a == list(a))
print(a is a)
print(a is list(a))

# dict key/value
test = {}
test['a'] = 1
test['b'] = 2
test['c'] = 3

for k,v in test.items():
    print(k,v)


