# 팀 결성

# 0번부터 N번까지의 번호
#
# 처음에는 모든 학생이 서로 다른 팀으로 구분되어 총 N+1개의 팀이 존재
#
# 팀 합치기 / 같은 팀 여부 확인 연산
#
# 선생님이 M개의 연산을 수행할 수 있을때 '같은 팀 여부 확인' 연산에 대한연산 결과를 출력하는 프로그램을 작성하시오

# 조건
# 첫째 줄에 n,m주어짐 (1<=n, m<=100000)
# 다음 M개의 줄에는 각각의 연산이 주어짐
# 팀합치기 연산은 0 a b가 주어짐 -> a,b팀을 합쳐라
# 같은 팀 여부 확인 연산 -> 1,a,b
#
# a,b,는 N이하의 양의 정수이다.
#
# 출력 조건
# 같은팀여부확인 연산에 대해 YES, NO 로 반환

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1
#
# No
# No
# YES

# print(parent)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_unit(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n + 1):
    parent[i] = i

for check in range(m):
    a,b,c = map(int,input().split())
    if a == 0:
        union_unit(parent,b,c)
    elif a == 1:
        if find_parent(parent, b) != find_parent(parent,c):
            print("NO")
        else:
            print("YES")

