# 간단한 다익스트라 알고리즘

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의갯수, 간선의 갯수
n,m = map(int, input().split())
# 시작 노드
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]



