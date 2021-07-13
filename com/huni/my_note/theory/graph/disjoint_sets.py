# 서로소 집합 알고리즘

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

for i in range(1, v+1):
    parent[i] = i

# union 연산
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1,v+1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

print()

# 6 4
# 1 4
# 2 3
# 2 4
# 5 6

# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 2 1 5 5

################################
## 경로 압축 방식
################################
# 각 원소가 속한 집합: 1 1 1 1 5 5
# 부모 테이블: 1 1 1 1 5 5




