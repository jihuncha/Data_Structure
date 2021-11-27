# 문제 설명
# 사회적 거리 유지를 위해 공연 관람객들의 좌석을 배정하려 합니다.
#
# 공연장의 각 좌석은 1 x 1 크기 정사각형 모양이며, 전체 좌석은 n x n 크기 정사각 격자 모양입니다. 관람객에게 좌석을 배정하는 규칙은 다음과 같습니다.
#
# 제일 처음 입장하는 관람객은 1행 1열 좌석을 배정받습니다.
# 두 번째 관람객부터는 먼저 좌석을 배정받은 다른 관람객 중 가장 가까운 관람객까지의 거리가 최대인 좌석을 배정합니다.
# 만약 그런 좌석이 여러 개라면 열 번호가 가장 작은 좌석을 배정합니다.
# 만약 열 번호가 가장 작은 좌석이 여러 개라면 행 번호가 가장 작은 좌석을 배정합니다.
# 두 좌석 사이의 거리는 행 번호 차이 + 열 번호 차이입니다.
# 예를 들어 [2행, 3열]과 [5행, 1열] 사이의 거리는 |2 - 5| + |3 - 1| = 5입니다(| |는 절댓값 기호입니다).
# 다음은 5 x 5 크기 관람석에 좌석을 배정하는 예시입니다.

# 제한사항
# n은 5 이상 50 이하인 자연수입니다.
# k는 1 이상 n2 이하인 자연수입니다.
# 정답은 [행 번호, 열 번호] 형태로 return 해주세요.


# n	k	result
# 5	12	[4,4]
# 5	16	[1,2]
# 6	13	[4,5]


n = 5
k = 12
#
# n = 5
# k = 16
#
# n = 6
# k = 13

import copy
def solution(n, k):

    # 맵핑할 리스트
    result = [[0] * (n+1) for _ in range(n + 1)]

    # 시작지점
    result[1][1] = 1
    # stack에 시작지점을 담아준다.
    stack = [(1,1)]

    # 가장 먼 거리 체크하는 로직
    def checkDist():
        # stack 보존을 위해 copy
        my_stack = copy.deepcopy(stack)
        # 거리값 체크를 위한 distance 배열 초기화
        distance = [[0] * (n + 1) for _ in range(n + 1)]

        # 가장 긴 거리값 체크
        max_distance = 0

        # stack에서 하나씩 꺼내주면서 해당 위치에서 거리의 최대값을 구한다.
        while my_stack:
            temp = my_stack.pop()
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    # 이미 누가 앉아있는 경우 (방문 처리)
                    if result[i][j] != 0:
                        continue
                    temp_dist = abs(i - temp[0]) + abs(j - temp[1])
                    # 이미 distance 가 맵핑되어 있는 경우는 최소 거리를 구해준다
                    if distance[i][j] != 0:
                        distance[i][j] = min(distance[i][j], temp_dist)
                    else:
                        distance[i][j] = temp_dist

        # 최대거리인 것들 list로 담는다
        check_list = []
        # 2차원 배열에서 최대 거리 체크
        max_distance = max(map(max, distance))
        for i in range(1, n+1):
            for j in range(1, n+1):
                if distance[i][j] == max_distance:
                    check_list.append((i,j))

        # sorting
        check_list.sort(key=lambda x : (x[1],x[0]))

        return [check_list[0][0], check_list[0][1]]

    for i in range(2, k+1):
        # 결과 좌표값 (가장먼곳)
        temp = checkDist()
        # 원하는 값(k)번째 행을 실행한 경우 빠져나간다
        if i == k:
            return temp
        # result에 맵핑 해준다.
        result[temp[0]][temp[1]] = i
        # stack에 해당 맵핑 위치 추가 해준다.
        stack.append(temp)
    return []


print(solution(n,k))