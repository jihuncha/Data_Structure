# https://programmers.co.kr/learn/courses/30/lessons/43162

# 네트워크
#
# 문제 설명
# 네트워크란 컴퓨터 상호 간에 정보를 교환할 수 있도록 연결된 형태를 의미합니다.
#
# 예를 들어, 컴퓨터 A와 컴퓨터 B가 직접적으로 연결되어있고,
#
# 컴퓨터 B와 컴퓨터 C가 직접적으로 연결되어 있을 때 컴퓨터 A와 컴퓨터 C도 간접적으로 연결되어 정보를 교환할 수 있습니다.
#
# 따라서 컴퓨터 A, B, C는 모두 같은 네트워크 상에 있다고 할 수 있습니다.
#
# 컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때, 네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
#
# 제한사항
# 컴퓨터의 개수 n은 1 이상 200 이하인 자연수입니다.
# 각 컴퓨터는 0부터 n-1인 정수로 표현합니다.
# i번 컴퓨터와 j번 컴퓨터가 연결되어 있으면 computers[i][j]를 1로 표현합니다.
# computer[i][i]는 항상 1입니다.

# 입출력 예
# n	computers	return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1

#############################
# 방문 여부 체크하면서
# bfs 수행
# 내가 맞게 한건가?? 그냥 정답만 잘된듯..?
#############################

def solution(n, computers):
    answer = 0
    # 방문 여부 체크할 내용
    visited = [False]* n

    # bfs
    def bfs(x):
        # 방문처리
        visited[x] = True
        # index와 값으로 체크
        for idx,i in enumerate(computers[x]):
            # index가 같은 경우는 수행 필요없음(나자신) -> 사실 visited에서 체크해서 필요없을듯?
            # 방문하지 않았고 연결되어있는(1)인 경우 다음 index에 동일한 작업 수행
            if idx != x and not visited[idx] and i == 1:
                bfs(idx)

    for k in range(n):
        # 방문하지 않은경우 수행하고 체크한다.
        if not visited[k]:
            bfs(k)

            answer+=1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
# print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


########### 다른 사람 풀이
# 나랑 비슷한듯?
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def dfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1

            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            dfs(computers, visited, i)
            answer +=1
        i+=1
    return answer

#### 2.플루이드-워셜 알고리즘 이라는데???
# ???????????백만개
def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))