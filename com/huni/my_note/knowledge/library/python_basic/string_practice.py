import re

b = 'zbdaf'
print("".join(sorted(b)))

a = ['ccc', 'aaaa', 'bb', 'd']
print(sorted(a, key=len))

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
 # 정규식 \w 는 단어 문자 // ^ not을 의미
words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()]

print(words)
# ['bob', 'hit', 'a', 'ball', 'the', 'hit', 'ball', 'flew', 'far', 'after', 'it', 'was', 'hit']