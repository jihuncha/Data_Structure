### 탐색
    * 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
    * 프로그래밍에서는 그래프, 트리에서 찾는 과정이 많다

### 탐색의 종류
    * 깊이 우선 탐색 (DFS - Depth First Search)
        - 주로 stack이나 재귀로 구현. 백트래킹으로 뛰어난 효용을 보임
        - 코딩테스트에서는 재귀로 하는 것이 더 선호
    * 너비 우선 탐색 (BFS - Breadth First Search)
        - 주로 Queue로 구현. 그래프의 최단 경로를 구하는 문제에서 사용
        - 다익스트라 알고리즘

### 그래프

[참고] (https://codermun-log.tistory.com/288)

* Node(노드) 와 Edge(간선)으로 표현. 노드를 정점(Vertex)라고도 한다.
* V(Vertex) - 그래프 안의 모든 노드의 합
* E(Edge) - 모든 간선의 합
* 그래프는 2가지 방식으로 표현 가능
    1. 인접 행렬(Adjacency Materix) - 2차원 배열로 그래프 연결 관계 표현
       * 장점
         1. 두 정점을 연결하는 간선을 조회할 때 O(1) 시간복잡도
         2. 정점(i)의 차수를 구할 때는 다음과 같이 인접행렬(M)의 i번째 행의 값을 모두 더하면 되므로 O(n)의 시간복잡도
       * 단점
         1. 간선의 수와 무관하게 항상 n² 크기의 2차원 배열이 필요하므로 메모리 공간이 낭비
         2. 그래프의 모든 간선의 수를 알아내려면 인접행렬 전체를 확인해야 하므로 O(n²)의 시간이 소요
    2. 인접 리스트(Adjacency List) - 리스트로 그래프 연결 관계 표현
       * 장점
         1. 존재하는 간선만 관리하면 되므로 메모리 사용 측면에서 보다 효율적
         2. 그래프의 모든 간선의 수를 알아내려면 각 정점의 헤더 노드부터 모든 인접리스트를 탐색해야 하므로 O(n+e)의 시간이 소요
       * 단점
         1. 두 정점을 연결하는 간선을 조회하거나 정점의 차수를 알기 위해서는 정점의 인접 리스트를 탐색해야 하므로 정점의 차수만큼의 시간이 필요 - O(degree(v))
         2. 구현이 비교적 어렵다
       

* 인접 행렬 방식 예제

~~~python
INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
~~~

* 인접 리스트 방식 예제

~~~python
graph = [[] for _ in range(3)]

#노드와 거리
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장
graph[2].append((0,5))
~~~

### DFS

* 재귀 구조의 DFS
~~~python
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def recursive_dfs(v, discoverd=[]):
    discoverd.append(v)
    for w in graph[v]:
        if w not in discoverd:
            recursive_dfs(w, discoverd)
    return discoverd

#[1, 2, 5, 6, 7, 3, 4]
print(recursive_dfs(1))
~~~

* stack DFS
~~~python
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def iterative_dfs(start_v):
    discoverd = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discoverd:
            discoverd.append(v)
            for w in graph[v]:
                stack.append(w)
                
    return discoverd

# [1, 4, 3, 5, 7, 6, 2]
print(iterative_dfs(1))
~~~

#### 결과 값이 다른 이유?
    - 재귀 DFS는 사전적 순로 방문했지만, 반복 DFS는 역순으로 방문하였기 때문
    
### BFS

* Queue BFS
~~~python
graph = {
    1: [2,3,4],
    2: [5],
    3: [5],
    4: [],
    5: [6,7],
    6: [],
    7: [3],
}

def iterative_bfs(start_v):
    discoverd = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoverd:
                discoverd.append(w)
                queue.append(w)
              
    return discoverd

# [1, 2, 3, 4, 5, 6, 7]
print(iterative_bfs(1))
~~~

#### 백트래킹
    * 해결책에 대한 후보를 구축해 나아가다가 가능성이 없다고 판단되는 즉시 후보를 포기 (백트랙) 해 정답을 찾아가는 방식
    * 범용적인 알고리즘으로 제약 충족 문제(Constraint Satisfaction Problems) 에 유용

