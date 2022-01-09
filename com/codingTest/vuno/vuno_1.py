# 신경망

# 4
# 3 4 4 2
# 36

# 5
# 1 2 4 8 1
# 50

# 3
# 1 9 1
# 18

n = int(input())
layers = [int(value) for value in input().split() ]

answer = 0

for i in range(n-1):
    answer += layers[i] * layers[i+1]

print(answer)


