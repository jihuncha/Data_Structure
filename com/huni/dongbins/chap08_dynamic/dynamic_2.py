# 1로 만들기

# input 26

# output 3

n = int(input())

# print(n)

temp = [0] * 30001

for i in range(2,n+1):
    temp[i] = temp[i-1] + 1

    if i % 2 == 0:
        temp[i] = min(temp[i], temp[i // 2] + 1)
    if i % 3 == 0:
        temp[i] = min(temp[i], temp[i // 3] + 1)
    if i % 5 == 0:
        temp[i] = min(temp[i], temp[i // 5] + 1)

# print(temp[1])
print(temp[n])
