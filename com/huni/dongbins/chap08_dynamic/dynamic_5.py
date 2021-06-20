# 효율적인 화폐 구성

# 2 15
# 2
# 3
#
# 5
#
# 3 4
# 3
# 5
# 7
#
# -1

n, goal = map(int, input().split())

array = [int(input()) for _ in range(n)]

print(n, goal, array)

d = [1e9] * (goal + 1)

d[0] = 0
# 2,3, .... 탐색
for i in range(n):
    # 2,3부터 목적지 까지 탐색
    for j in range(array[i], goal + 1):
        print(j, array[i], d)
        # 해당 위치의 숫자 (j - array[i] 가 뺸숫자임.)
        if d[j - array[i]] != 1e9:
            d[j] = min(d[j], d[j - array[i]] + 1)

    print(i, d)

if d[goal] == 1e9:
    print(-1)
else:
    print(d[goal])

