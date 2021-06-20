# 성적이 낮은 순서로 학생 출력하기

# input
# 2
# 홍길동 95
# 이순신 77

# output
# 이순신 홍길동



n = int(input())

data = []
for i in range(n):
    data.append(list((input().split())))

result = sorted(data, key=lambda x: int(x[1]))
print(result)

for temp in result:
    print(temp[0], end=' ')
# print(data)