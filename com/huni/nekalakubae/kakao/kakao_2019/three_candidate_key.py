# https://programmers.co.kr/learn/courses/30/lessons/42890

# 후보키

# 프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.
#
# 그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.
#
# 후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.
#
# 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
# 유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
# 최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
# 즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
# 제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

# three_img_1 참고

# 위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 "학번"을 가지고 있다. 따라서 "학번"은 릴레이션의 후보 키가 될 수 있다.
# 그다음 "이름"에 대해서는 같은 이름("apeach")을 사용하는 학생이 있기 때문에, "이름"은 후보 키가 될 수 없다.
# 그러나, 만약 ["이름", "전공"]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다.
# 물론 ["이름", "전공", "학년"]을 함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다.
# 따라서, 위의 학생 인적사항의 후보키는 "학번", ["이름", "전공"] 두 개가 된다.
#
# 릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.
#
# 제한사항
# relation은 2차원 문자열 배열이다.
# relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
# relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
# relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
# relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)

# 입출력 예
# relation	result
# [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	2

# 입출력 예 설명
# 입출력 예 #1
# 문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.

## dfs..?
# 조합만드는거를 해결못햇음..구현이 아직도 미숙한듯

import itertools
def solution(relation):
    answer = 0

    dic = {}
    result_comlumn_temp = []

    #컬럼 갯수
    count_column = [x for x in range(len(relation[0]))]

    print(count_column)

    #숫자로 combination 작성 -> 모든 행의 조합은 필요없다 (-1 추가)
    com_list = []
    for i in range(len(count_column) - 1):
        com_list += list(itertools.combinations(count_column, i+1))
    print(com_list)

    result_list = []
    for i in com_list:
        key_candidate = True
        temp_list = []
        str_temp = ''
        for check in relation:
            for j in i:
                str_temp += check[j] + '/'
            if str_temp in temp_list:
                key_candidate = False
                break
            temp_list.append(str_temp)
            str_temp = ''
        if key_candidate:
            str_result = ''.join([str(s) for s in i])
            print(str_result)
            if len(result_list) == 0:
                result_list.append(str_result)
            temp_check = False
            for i in result_list:
                if i in str_result:
                    temp_check = True
                    break
                if not temp_check:
                    result_list.append(str_result)

            # if any(result_list, str_result):
            #     print("test")
            # print(temp_list)
    print(result_list)

    # real_list = []
    # for i in result_list:
    #     change_str = '/'.join([str(k) for k in i])
    #     print(change_str)
    #     if len(real_list) == 0:
    #         real_list.append(change_str)
    #
    # print(real_list)
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

from itertools import combinations

def solution(relation):
    answer = 0

    #컬럼 갯수
    temp = [i for i in range(len(relation[0]))]
    # print(temp)

    # 조합담을 list
    combi_lists = list()

    # 조합 생성 -> combination으로 1~전체 갯수만큼 숫자로 생성 (index)
    for cnt in range(1, len(relation[0]) + 1):
        combi_lists.append(list(combinations(temp, cnt)))
    # print(combi_lists)

    # 조합리스트를 문자열로 변경
    combi_str_list = list()
    for combi_list in combi_lists:
        for i in combi_list:
            combi_str_list.append(''.join(map(str, i)))

    # print(combi_str_list)
    # ['0', '1', '2', '3', '01', '02', '03', '12', '13', '23', '012', '013', '023', '123', '0123']

    while len(combi_str_list) > 0:
        candidate_key = list()
        is_candidate_key = True

        for r in relation:
            key = ""
            for j in combi_str_list[0]:
                key += r[int(j)]
            # print(key)

            if key in candidate_key:
                is_candidate_key = False
                break
            else:
                candidate_key.append(key)

        if is_candidate_key is False:
            del combi_str_list[0]
            continue

        str_list = list(combi_str_list[0])
        # print(str_list)

        combi_str_list = [s for s in combi_str_list if any(str not in s for str in str_list)]
        # print(combi_str_list)

        answer += 1

    return answer


# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))

