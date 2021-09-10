# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
#
# 0
# 2
# 3
# 1
# 2
# 4
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline

n,m = map(int, input().split())
index = int(input())

data = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = list(map(int,input().split()))
    data[a].append((b,c))

# visited = [False] * (n+1)
result = [INF] * (n+1)

def dijstra(start:int):
    result[start] = 0
    stack = [(0, start)]

    while stack:
        dist, now = heapq.heappop(stack)
        # print(temp)

        if result[now] < dist:
            continue

        for j in data[now]:
            cost = dist + j[1]
            if cost < result[j[0]]:
                result[j[0]] = cost
                heapq.heappush(stack, (cost, j[0]))

dijstra(index)
print(result)

# def get_smallest_node():
#     temp = INF
#     temp_index = 0
#     for i in range(1,n+1):
#         if not visited[i] and result[i] <= temp:
#             temp = result[i]
#             temp_index = i
#     return temp_index
#
# def dijstra(start:int):
#     result[start] = 0
#     visited[start] = True
#
#     stack = []
#     #인접 노드 확인 -> 초기화
#     for i in data[start]:
#         result[i[0]] = i[1]
#
#     for check in range(n-1):
#         now = get_smallest_node()
#         visited[now] = True
#
#         for j in data[now]:
#             a,b = j
#             # print(a,b)
#             if result[a] > result[now] + b:
#                 result[a] = result[now] + b
#
#
#
# dijstra(index)
# print(result)



# 플로이드

# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2


