# 서로소 집합 알고리즘 사이클 체크

# 특정원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
    # if parent[x] != x:
    #     return find_parent(parent, parent[x])
    # return x

    # find 함수가 비효율적 (시간복잡도 O(V))

    # 경로 압축 방식 사용 (Path Compression)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    # 해당 노드의 루트 노드가 바로 부모 노드가 된다.
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드/간선의 개수 입력
v,e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False # 사이클 발생 여부

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발행하지 않았다면 합집합 수행
    else:
        union_parent(parent,a,b)

if cycle:
    print("사이클!!")
else:
    print("no cycle!!")

# 3 3
# 1 2
# 1 3
# 2 3
