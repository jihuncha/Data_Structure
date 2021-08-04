# https://programmers.co.kr/learn/courses/30/lessons/72412

# 순위 검색

# 문제 설명
# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
#
# 카카오는 하반기 경력 개발자 공개채용을 진행 중에 있으며 현재 지원서 접수와 코딩테스트가 종료되었습니다.
# 이번 채용에서 지원자는 지원서 작성 시 아래와 같이 4가지 항목을 반드시 선택하도록 하였습니다.
#
# 코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
# 지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
# 지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
# 선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.
# 인재영입팀에 근무하고 있는 니니즈는 코딩테스트 결과를 분석하여 채용에 참여한
# 개발팀들에 제공하기 위해 지원자들의 지원 조건을 선택하면 해당 조건에 맞는 지원자가 몇 명인 지 쉽게 알 수 있는 도구를 만들고 있습니다.
# 예를 들어, 개발팀에서 궁금해하는 문의사항은 다음과 같은 형태가 될 수 있습니다.
# 코딩테스트에 java로 참여했으며, backend 직군을 선택했고, junior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 50점 이상 받은 지원자는 몇 명인가?
#
# 물론 이 외에도 각 개발팀의 상황에 따라 아래와 같이 다양한 형태의 문의가 있을 수 있습니다.
#
# 코딩테스트에 python으로 참여했으며, frontend 직군을 선택했고, senior 경력이면서, 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
# 코딩테스트에 cpp로 참여했으며, senior 경력이면서, 소울푸드로 pizza를 선택한 사람 중 코딩테스트 점수를 100점 이상 받은 사람은 모두 몇 명인가?
# backend 직군을 선택했고, senior 경력이면서 코딩테스트 점수를 200점 이상 받은 사람은 모두 몇 명인가?
# 소울푸드로 chicken을 선택한 사람 중 코딩테스트 점수를 250점 이상 받은 사람은 모두 몇 명인가?
# 코딩테스트 점수를 150점 이상 받은 사람은 모두 몇 명인가?
# 즉, 개발팀에서 궁금해하는 내용은 다음과 같은 형태를 갖습니다.

# * [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?

# [문제]
# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info, 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query가 매개변수로 주어질 때,
# 각 문의조건에 해당하는 사람들의 숫자를 순서대로 배열에 담아 return 하도록 solution 함수를 완성해 주세요.
#
# [제한사항]
# info 배열의 크기는 1 이상 50,000 이하입니다.
# info 배열 각 원소의 값은 지원자가 지원서에 입력한 4가지 값과 코딩테스트 점수를 합친 "개발언어 직군 경력 소울푸드 점수" 형식입니다.
# 개발언어는 cpp, java, python 중 하나입니다.
# 직군은 backend, frontend 중 하나입니다.
# 경력은 junior, senior 중 하나입니다.
# 소울푸드는 chicken, pizza 중 하나입니다.
# 점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
# 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
# query 배열의 크기는 1 이상 100,000 이하입니다.
# query의 각 문자열은 "[조건] X" 형식입니다.
# [조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 형식의 문자열입니다.
# 언어는 cpp, java, python, - 중 하나입니다.
# 직군은 backend, frontend, - 중 하나입니다.
# 경력은 junior, senior, - 중 하나입니다.
# 소울푸드는 chicken, pizza, - 중 하나입니다.
# '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
# X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.
# 각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.
# 예를 들면, "cpp and - and senior and pizza 500"은 "cpp로 코딩테스트를 봤으며,
# 경력은 senior 이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 500점 이상 받은 사람은 모두 몇 명인가?"를 의미합니다.

# 입출력 예
# info	query	result
# ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
# ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# [1,1,1,1,2,4]
#
# 입출력 예에 대한 설명
# 지원자 정보를 표로 나타내면 다음과 같습니다.
#
# 언어	직군	경력	소울 푸드	점수
# java	backend	junior	pizza	150
# python	frontend	senior	chicken	210
# python	frontend	senior	chicken	150
# cpp	backend	senior	pizza	260
# java	backend	junior	chicken	80
# python	backend	senior	chicken	50
#
# "java and backend and junior and pizza 100" : java로 코딩테스트를 봤으며, backend 직군을 선택했고 junior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 100점 이상 받은 지원자는 1명 입니다.
# "python and frontend and senior and chicken 200" : python으로 코딩테스트를 봤으며, frontend 직군을 선택했고, senior 경력이면서 소울 푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 200점 이상 받은 지원자는 1명 입니다.
# "cpp and - and senior and pizza 250" : cpp로 코딩테스트를 봤으며, senior 경력이면서 소울푸드로 pizza를 선택한 지원자 중 코딩테스트 점수를 250점 이상 받은 지원자는 1명 입니다.
# "- and backend and senior and - 150" : backend 직군을 선택했고, senior 경력인 지원자 중 코딩테스트 점수를 150점 이상 받은 지원자는 1명 입니다.
# "- and - and - and chicken 100" : 소울푸드로 chicken을 선택한 지원자 중 코딩테스트 점수를 100점 이상을 받은 지원자는 2명 입니다.
# "- and - and - and - 150" : 코딩테스트 점수를 150점 이상 받은 지원자는 4명 입니다.

import bisect

input_str = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query_str = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []

    db = {}

    info.sort(key=lambda x: int(x.split(' ')[-1]))

    for check in info:
        temp_str = check.split(' ')[:-1]
        print(temp_str)

    # temp_info = []
    # temp_num_info = []
    # info.sort(key=lambda x: int(x.split(' ')[-1]))
    #
    # for check in info:
    #     temp_list = list(map(str, check.split()))
    #     temp_info.append(temp_list)
    #     temp_num_info.append(int(temp_list[-1]))
    #
    # # temp_info.sort(key=lambda x : int(x[0]))
    # # print(temp_info)
    # # temp_num_info.sort()
    # # print(temp_num_info)
    #
    # for i in query:
    #     count = 0
    #     change_str = i.replace(' and ', ' ')
    #     temp_query = list(map(str, change_str.split(' ')))
    #     # temp_query.reverse()
    #     # print(temp_query)
    #     check = int(temp_query[-1])
    #     index = bisect.bisect_left(temp_num_info, check)
    #     # print(check)
    #     # print(index)
    #     # print(temp_info[index:])
    #     for j in temp_info[index:]:
    #         if (j[0] == temp_query[0] or temp_query[0] == '-') and (j[1] == temp_query[1] or temp_query[1] == '-') \
    #             and (j[2] == temp_query[2] or temp_query[2] == '-') and (j[3] == temp_query[3] or temp_query[3] == '-'):
    #             count +=1
    #     answer.append(count)

    return answer

# print(solution(input_str, query_str))





##############
# 1차 시기

# def solution(info, query):
#     answer = []

#     temp_info = []
#     temp_num_info = []

#     for check in info:
#         temp_list = list(map(str, check.split()))
#         temp_list.reverse()
#         temp_info.append(temp_list)
#         temp_num_info.append(int(temp_list[0]))

#     temp_info.sort(key=lambda x : int(x[0]))
#     # print(temp_info)
#     temp_num_info.sort()
#     # print(temp_num_info)

    # for i in query:
    #     count = 0
    #     change_str = i.replace(' and ', ' ')
    #     temp_query = list(map(str, change_str.split(' ')))
    #     temp_query.reverse()
    #     # print(temp_query)
    #     check = int(temp_query[0])
    #     index = bisect.bisect_left(temp_num_info, check)
    #     # print(index)
    #     # print(temp_info[index:])
    #     for j in temp_info[index:]:
    #         if (j[1] == temp_query[1] or temp_query[1] == '-') and (j[2] == temp_query[2] or temp_query[2] == '-') \
    #             and (j[3] == temp_query[3] or temp_query[3] == '-') and (j[4] == temp_query[4] or temp_query[4] == '-'):
    #             count +=1
    #     answer.append(count)

#     return answer

# 테스트 1 〉	통과 (0.10ms, 10.4MB)
# 테스트 2 〉	통과 (0.08ms, 10.4MB)
# 테스트 3 〉	통과 (0.39ms, 10.5MB)
# 테스트 4 〉	통과 (7.35ms, 10.5MB)
# 테스트 5 〉	통과 (11.47ms, 10.5MB)
# 테스트 6 〉	통과 (25.38ms, 10.7MB)
# 테스트 7 〉	통과 (12.94ms, 10.6MB)
# 테스트 8 〉	통과 (68.65ms, 13MB)
# 테스트 9 〉	통과 (61.07ms, 13.3MB)
# 테스트 10 〉	통과 (71.29ms, 13.3MB)
# 테스트 11 〉	통과 (21.36ms, 10.5MB)
# 테스트 12 〉	통과 (22.77ms, 10.6MB)
# 테스트 13 〉	통과 (12.00ms, 10.6MB)
# 테스트 14 〉	통과 (46.14ms, 11.6MB)
# 테스트 15 〉	통과 (59.71ms, 11.6MB)
# 테스트 16 〉	통과 (11.20ms, 10.5MB)
# 테스트 17 〉	통과 (26.10ms, 10.7MB)
# 테스트 18 〉	통과 (49.15ms, 11.6MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)


######### 2차 시기
# 이게 최선인거같은데..ㅠ

# def solution(info, query):
#     answer = []
#
#     temp_info = []
#     temp_num_info = []
#     info.sort(key=lambda x: int(x.split(' ')[-1]))
#
#     for check in info:
#         temp_list = list(map(str, check.split()))
#         temp_info.append(temp_list)
#         temp_num_info.append(int(temp_list[-1]))
#
#     # temp_info.sort(key=lambda x : int(x[0]))
#     # print(temp_info)
#     # temp_num_info.sort()
#     # print(temp_num_info)
#
#     for i in query:
#         count = 0
#         change_str = i.replace(' and ', ' ')
#         temp_query = list(map(str, change_str.split(' ')))
#         # temp_query.reverse()
#         # print(temp_query)
#         check = int(temp_query[-1])
#         index = bisect.bisect_left(temp_num_info, check)
#         # print(check)
#         # print(index)
#         # print(temp_info[index:])
#         for j in temp_info[index:]:
#             if (j[0] == temp_query[0] or temp_query[0] == '-') and (j[1] == temp_query[1] or temp_query[1] == '-') \
#                 and (j[2] == temp_query[2] or temp_query[2] == '-') and (j[3] == temp_query[3] or temp_query[3] == '-'):
#                 count +=1
#         answer.append(count)
#
#     return answer
#
# print(solution(input_str, query_str))

# 테스트 1 〉	통과 (0.09ms, 10.5MB)
# 테스트 2 〉	통과 (0.09ms, 10.5MB)
# 테스트 3 〉	통과 (0.36ms, 10.4MB)
# 테스트 4 〉	통과 (3.35ms, 10.6MB)
# 테스트 5 〉	통과 (9.85ms, 10.5MB)
# 테스트 6 〉	통과 (20.05ms, 10.7MB)
# 테스트 7 〉	통과 (11.01ms, 10.6MB)
# 테스트 8 〉	통과 (47.87ms, 13MB)
# 테스트 9 〉	통과 (46.93ms, 13.1MB)
# 테스트 10 〉	통과 (55.17ms, 13MB)
# 테스트 11 〉	통과 (9.38ms, 10.6MB)
# 테스트 12 〉	통과 (19.09ms, 10.5MB)
# 테스트 13 〉	통과 (10.88ms, 10.6MB)
# 테스트 14 〉	통과 (40.09ms, 11.6MB)
# 테스트 15 〉	통과 (43.19ms, 11.6MB)
# 테스트 16 〉	통과 (9.88ms, 10.5MB)
# 테스트 17 〉	통과 (20.30ms, 10.5MB)
# 테스트 18 〉	통과 (40.39ms, 11.6MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	실패 (시간 초과)

from itertools import combinations


### 풀이
def solution(info, query):
    answer = []
    db = {}
    for i in info:  # info에 대해 반복
        temp = i.split()
        conditions = temp[:-1]  # 조건들만 모으고, 점수 따로
        score = int(temp[-1])
        for n in range(5):  # 조건들에 대해 조합을 이용해서
            combi = list(combinations(range(4), n))
            print(combi)
            for c in combi:
                t_c = conditions.copy()
                print("t_c ", t_c)
                for v in c:  # '-'를 포함한 새로운 조건을 만들어냄.
                    t_c[v] = '-'
                changed_t_c = '/'.join(t_c)
                if changed_t_c in db:  # 모든 조건의 경우에 수에 대해 딕셔너리
                    db[changed_t_c].append(score)
                else:
                    db[changed_t_c] = [score]

    for value in db.values():  # 딕셔너리 내 모든 값 정렬
        value.sort()
    print(db)

    for q in query:  # query의 모든 조건에 대해서
        qry = [i for i in q.split() if i != 'and']
        qry_cnd = '/'.join(qry[:-1])
        qry_score = int(qry[-1])
        if qry_cnd in db:  # 딕셔너리 내에 값이 존재한다면,
            data = db[qry_cnd]
            if len(data) > 0:
                start, end = 0, len(data)  # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(data):
                    if data[(start + end) // 2] >= qry_score:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data) - start)  # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)

    return answer

print(solution(input_str, query_str))

## 속도
# 테스트 1 〉	통과 (0.50ms, 10.5MB)
# 테스트 2 〉	통과 (0.46ms, 10.5MB)
# 테스트 3 〉	통과 (0.53ms, 10.5MB)
# 테스트 4 〉	통과 (1.97ms, 10.5MB)
# 테스트 5 〉	통과 (5.07ms, 10.5MB)
# 테스트 6 〉	통과 (6.85ms, 10.6MB)
# 테스트 7 〉	통과 (7.57ms, 10.7MB)
# 테스트 8 〉	통과 (57.75ms, 11.5MB)
# 테스트 9 〉	통과 (84.00ms, 11.5MB)
# 테스트 10 〉	통과 (55.57ms, 11.7MB)
# 테스트 11 〉	통과 (4.37ms, 10.6MB)
# 테스트 12 〉	통과 (8.54ms, 10.6MB)
# 테스트 13 〉	통과 (4.71ms, 10.8MB)
# 테스트 14 〉	통과 (30.41ms, 10.9MB)
# 테스트 15 〉	통과 (33.57ms, 11MB)
# 테스트 16 〉	통과 (5.35ms, 10.6MB)
# 테스트 17 〉	통과 (11.86ms, 10.6MB)
# 테스트 18 〉	통과 (28.93ms, 11MB)
# 효율성  테스트
# 테스트 1 〉	통과 (1060.06ms, 42MB)
# 테스트 2 〉	통과 (1038.56ms, 42.4MB)
# 테스트 3 〉	통과 (1124.74ms, 42.4MB)
# 테스트 4 〉	통과 (1127.51ms, 42.1MB)