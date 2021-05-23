# 자물쇠와 열쇠

# https://programmers.co.kr/learn/courses/30/lessons/60059

# 고고학자인 "튜브"는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다.
#
# 그런데 문을 열려고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.
#
# 잠겨있는 자물쇠는 격자 한 칸의 크기가 1 x 1인 N x N 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 M x M 크기인 정사각 격자 형태로 되어 있습니다.
#
# 자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다.
#
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다.
#
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
#
# 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다.
#
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
#
# 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
#
# 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
#
# key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
#
#
# lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
#
# M은 항상 N 이하입니다.
#
# key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
#
# 0은 홈 부분, 1은 돌기 부분을 나타냅니다.
#
# 입출력 예
#
# key	lock	result
# [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]	true
#
# # https://grepp-programmers.s3.amazonaws.com/files/production/469703690b/79f2f473-5d13-47b9-96e0-a10e17b7d49a.jpg
#
# key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.

# 타임아웃 / 런타임 에러 뜬당 / 실패 다뜬당
# 이게 한계 ㅠㅠ
# 먼저 key의 돌기 부분의 갯수가 lock 의 홉 부분과 일치해야한다.
def solution(key, lock):
    global answer
    answer = False

    # key_list 제작 함수
    # key 의 경우는 True 로 해서 1인 부분 체크
    # lock의 경우는 False 로 해서 0인 부분 체크
    def make_key_list(key_data, one_or_zero):
        result_key_list = []
        for i in range(len(key_data)):
            for j in range(len(key_data)):
                if one_or_zero:
                    if key_data[i][j] == 1:
                        result_key_list.append([i, j])
                else:
                    if key_data[i][j] == 0:
                        result_key_list.append([i, j])
        return result_key_list

    # lock을 확인하여 실패 케이스 체크
    suc_list = make_key_list(lock, False)
    # 원본 손상 방지용
    temp = key
    # key_list 초기 생성
    key_list = make_key_list(temp, True)

    # rotate 결과 반환 함수
    def rotate(data):
        # 0으로 초기화
        result_list = [[0] * len(key[0]) for _ in range(len(key))]
        for i in range(0, len(key)):
            # 행의수
            for j in range(0, len(key[0])):
                result_list[j][len(key) - i - 1] = data[i][j]

        return result_list

    # 방문한 좌표 체크
    visited_list = []
    # 상하좌우 이동
    def check_and_move(search_key):
        global answer
        # 이미 방문한적이 있는 경우는 빠져나가자.
        if search_key in visited_list:
            return

        # 방문한 좌표 체크
        visited_list.append(search_key)

        # 상하 좌우로 이동
        dx = [0,0,1,-1]
        dy = [1,-1,0,0]

        for i in range(4):
            temp_key_list = []
            for k in search_key:
                x = dx[i] + k[0]
                y = dy[i] + k[1]
                # print(x,y)
                if x > len(key) - 1 or x < 0 or y > len(key) - 1 or y < 0:
                    continue
                temp_key_list.append([x,y])
            # 아무것도 없는 경우 벗어난다
            if len(temp_key_list) == 0:
                return
            # 결과를 발견한 경우
            if temp_key_list[:] == suc_list[:]:
                answer = True
                return
            # 벗어 나지 못한 경우는 다음 좌표에서 실행.
            check_and_move(temp_key_list)

    check_and_move(key_list)
    # print("================")
    for i in range(3):
        # 이미 결과가 true인 경우 할 필요없지
        if answer:
            break
        # 방문 list 초기화
        visited_list = []
        # temp를 회전하여 변경
        temp = rotate(temp)
        # key_list 새로 작성한다.
        key_list = make_key_list(temp, True)
        # 확인
        check_and_move(key_list)

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

# 테스트 1 〉	통과 (0.22ms, 10.3MB)
# 테스트 2 〉	실패 (15.08ms, 10.4MB)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (56.81ms, 10.4MB)
# 테스트 5 〉	실패 (시간 초과)
# 테스트 6 〉	실패 (2757.23ms, 13.4MB)
# 테스트 7 〉	실패 (시간 초과)
# 테스트 8 〉	실패 (시간 초과)
# 테스트 9 〉	실패 (시간 초과)
# 테스트 10 〉	실패 (런타임 에러)
# 테스트 11 〉	실패 (시간 초과)
# 테스트 12 〉	실패 (3.51ms, 10.3MB)
# 테스트 13 〉	실패 (시간 초과)
# 테스트 14 〉	통과 (41.89ms, 10.5MB)
# 테스트 15 〉	실패 (3809.00ms, 14MB)
# 테스트 16 〉	실패 (시간 초과)
# 테스트 17 〉	실패 (시간 초과)
# 테스트 18 〉	실패 (시간 초과)
# 테스트 19 〉	실패 (1.04ms, 10.3MB)
# 테스트 20 〉	실패 (시간 초과)
# 테스트 21 〉	실패 (시간 초과)
# 테스트 22 〉	실패 (시간 초과)
# 테스트 23 〉	통과 (84.21ms, 10.6MB)
# 테스트 24 〉	통과 (13.46ms, 10.4MB)
# 테스트 25 〉	실패 (시간 초과)
# 테스트 26 〉	실패 (시간 초과)
# 테스트 27 〉	실패 (시간 초과)
# 테스트 28 〉	실패 (시간 초과)
# 테스트 29 〉	통과 (156.43ms, 10.8MB)
# 테스트 30 〉	실패 (시간 초과)
# 테스트 31 〉	실패 (시간 초과)
# 테스트 32 〉	실패 (시간 초과)
# 테스트 33 〉	실패 (시간 초과)
# 테스트 34 〉	통과 (14.42ms, 10.5MB)
# 테스트 35 〉	통과 (59.47ms, 10.5MB)
# 테스트 36 〉	통과 (278.28ms, 10.7MB)
# 테스트 37 〉	통과 (235.10ms, 10.8MB)
# 테스트 38 〉	실패 (1.70ms, 10.2MB)