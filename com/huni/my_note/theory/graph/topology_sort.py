# 위상 정렬
import collections
from collections import deque

# 노드와 간선의 갯수 받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선의 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 간선의 정보 입력 받기
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b) #정점 A에서 B로 이동 가능
    # 진입차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 결과를 담을 리스트
    q = collections.deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드의 진입차수를 1씩 뺴기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0 이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    #위상 정렬 결과를 출력
    for i in result:
        print(i, end=' ')

topology_sort()

# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4
#
#
# 1 2 5 3 6 4 7



