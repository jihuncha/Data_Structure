# 위에서 아래로

#input
# 3
# 15
# 27
# 12
#
#output
# 27 15 12

n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data.sort(reverse=True)

for i in data:
    print(i, end=' ')
# print(data)