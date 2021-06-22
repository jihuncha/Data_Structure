# https://programmers.co.kr/learn/courses/30/lessons/43105

# 정수 삼각형

# 문제 설명
# sample.png 참고
#
# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중,
# 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다.
# 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.
# 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
#
# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# 삼각형의 높이는 1 이상 500 이하입니다.
# 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.
# 입출력 예
# triangle	result
# [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30

#### 타 문제랑 똑같음
# 근데 해당 풀이로 오류나서 새로 적용..
# 기존 코드는 뭐가 잘못된걸까

def solution(triangle):
    answer = 0

    # 전체 범위만큼
    # for i in range(1, len(triangle)):
    #     # next의 범위 i+1
    #     for j in range(i + 1):
    #         # 맨 왼쪽자리의 경우
    #         if j == 0:
    #             left = 0
    #         else:
    #             left = triangle[i - 1][j - 1]
    #         # 맨 오른쪽 자리의 경우
    #         if j == i:
    #             right = 0
    #         else:
    #             right = triangle[i - 1][j]
    #
    #         triangle[i][j] = triangle[i][j] + max(left, right)
    #
    # answer = max(triangle[len(triangle) - 1])

    # 전체 범위만큼
    for i in range(1, len(triangle)):
        # 해당 i번째 범위(1부터) 체크
        for j in range(len(triangle[i])):
            # 맨 왼쪽
            if j == 0:
                left = 0
            else:
                left = triangle[i - 1][j - 1]
            # 맨 오른쪽
            if j == len(triangle[i]) - 1:
                right = 0
            else:
                right = triangle[i - 1][j]
            # print("test - ", i, j, left, right)

            triangle[i][j] = max(triangle[i][j] + left, triangle[i][j] + right)

    answer = max(triangle[len(triangle) - 1])
    return answer



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

