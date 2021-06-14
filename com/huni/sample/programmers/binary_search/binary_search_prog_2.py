# https://programmers.co.kr/learn/courses/30/lessons/60060

# 가사 검색

# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
#
# 친구들로부터 천재 프로그래머로 불리는 "프로도"는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니
# 프로그램으로 개발해 달라는 제안을 받았습니다.
# 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다.
# 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다.
#
# 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.
#
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때,
#
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.
#
# 가사 단어 제한사항
# words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.

# 검색 키워드 제한사항
# queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
# 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
# 검색 키워드는 중복될 수도 있습니다.
# 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
# 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
# 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.
#
# 입출력 예
# words	queries	result
# ["frodo", "front", "frost", "frozen", "frame", "kakao"]	["fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]
#
# 입출력 예에 대한 설명
# "fro??"는 "frodo", "front", "frost"에 매치되므로 3입니다.
# "????o"는 "frodo", "kakao"에 매치되므로 2입니다.
# "fr???"는 "frodo", "front", "frost", "frame"에 매치되므로 4입니다.
# "fro???"는 "frozen"에 매치되므로 1입니다.
# "pro?"는 매치되는 가사 단어가 없으므로 0 입니다.

################
# 4단계 프로그래머스, 카카오 2020문제
# 효율성 2,3 실패
# trie 구조를 사용하라는데 처음 들어봄
# 학습 필요 문제!!
################

def solution(words, queries):
    answer = []
    dic = {}

    # 쿼리할 문장에서 하나씩 뺴온다
    for data in queries:
        # 이미 진행한적 있는 문자열인 경우 answer에 더해주고 continue 수행 - 시간 단축을 위함
        if data in dic:
            answer.append(dic[data])
            continue

        # ? 가 맨 앞 또는 맨뒤에 있으므로 해당 문자열 index 저장 (c,d)
        temp_len = len(data)
        check_first_last = data.index("?")
        count_check = data.count("?")
        if check_first_last > 0:
            # a,b = check_first_last, len(data)
            c,d = 0, temp_len - count_check
        else:
            # a,b = 0, count_check
            c,d = count_check, temp_len

        # 단어들을 탐색하면서 체크 한다.
        for j in words:
            # 해당 범위 단어가 동일하면서 길이가 같은 경우
            if data[c:d] == j[c:d] and len(j) == temp_len:
                # 딕셔너리에 존재하는 유무 체크
                if data in dic:
                    dic[data] += 1
                else:
                    dic[data] = 1

        if data in dic:
            answer.append(dic[data])
        else:
            answer.append(0)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))

# 초기 count사용
# 테스트 1 〉	통과 (0.39ms, 10.2MB)
# 테스트 2 〉	통과 (0.18ms, 10.2MB)
# 테스트 3 〉	통과 (0.20ms, 10.3MB)
# 테스트 4 〉	통과 (0.17ms, 10.1MB)
# 테스트 5 〉	통과 (0.26ms, 10.1MB)
# 테스트 6 〉	통과 (0.22ms, 10.2MB)
# 테스트 7 〉	통과 (7.21ms, 10.2MB)
# 테스트 8 〉	통과 (8.70ms, 10.2MB)
# 테스트 9 〉	통과 (10.43ms, 10.2MB)
# 테스트 10 〉	통과 (6.28ms, 10.3MB)
# 테스트 11 〉	통과 (5.97ms, 10.4MB)
# 테스트 12 〉	통과 (7.66ms, 10.3MB)
# 테스트 13 〉	통과 (127.44ms, 10.3MB)
# 테스트 14 〉	통과 (114.57ms, 10.3MB)
# 테스트 15 〉	통과 (137.89ms, 10.4MB)
# 테스트 16 〉	통과 (128.50ms, 10.3MB)
# 테스트 17 〉	통과 (116.82ms, 10.2MB)
# 테스트 18 〉	통과 (134.79ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	실패 (시간 초과)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	통과 (27.92ms, 13.5MB)
# 테스트 5 〉	통과 (43.52ms, 13.7MB)

# dic 사용했으나 2개 해결안됨..
# 테스트 1 〉	통과 (0.37ms, 10.3MB)
# 테스트 2 〉	통과 (0.15ms, 10.1MB)
# 테스트 3 〉	통과 (0.18ms, 10.2MB)
# 테스트 4 〉	통과 (0.18ms, 10.3MB)
# 테스트 5 〉	통과 (0.22ms, 10.2MB)
# 테스트 6 〉	통과 (0.19ms, 10.3MB)
# 테스트 7 〉	통과 (8.46ms, 10.2MB)
# 테스트 8 〉	통과 (7.01ms, 10MB)
# 테스트 9 〉	통과 (6.72ms, 10.3MB)
# 테스트 10 〉	통과 (5.81ms, 10.3MB)
# 테스트 11 〉	통과 (5.33ms, 10.2MB)
# 테스트 12 〉	통과 (4.89ms, 10.3MB)
# 테스트 13 〉	통과 (81.58ms, 10.2MB)
# 테스트 14 〉	통과 (96.48ms, 10.5MB)
# 테스트 15 〉	통과 (81.01ms, 10.6MB)
# 테스트 16 〉	통과 (92.38ms, 10.3MB)
# 테스트 17 〉	통과 (95.04ms, 10.4MB)
# 테스트 18 〉	통과 (63.19ms, 10.4MB)
# 효율성  테스트
# 테스트 1 〉	통과 (3055.88ms, 22.5MB)
# 테스트 2 〉	실패 (시간 초과)
# 테스트 3 〉	실패 (시간 초과)
# 테스트 4 〉	통과 (2.27ms, 13.3MB)
# 테스트 5 〉	통과 (5.71ms, 13.8MB)

#####################################################
# 이진 탐색을 통한 해결 가능
# 1. 각 단어를 길이로 나눔
# 2. 리스트 정렬 이후에 각 쿼리에 대해서 이진탐색을 사용
#
# ex 길이가 5인 단어끼리 배열하여 fro?? 인 경우 fro로 시작하는 단어를 탐색하면 됨
# -> fro로 시작하는 처음 단어 와 fro 로 시작하는 마지막 단어를 찾아 그 위치 차이를 계산한다.
#
# 또는 froaa 보다 크거나 같으면서 frozz보다 작거나 같은 단어를 찾는다.
#
# 접두사에 ?가 달린 경우도 고려하여 글자를 뒤집은걸로 같은 동작을 반복해주면된다.

import bisect

def count_by_range(a, left_value, right_value):
    right_index = bisect.bisect_right(a, right_value)
    left_index = bisect.bisect_left(a, left_value)

    return right_index - left_index


def solution(words, queries):
    answer = []

    length_list = [[] for _ in range(10001)]
    length_list_reverse = [[] for _ in range(10001)]

    for i in words:
        length_list[len(i)].append(i)
        length_list_reverse[len(i)].append(i[::-1])

    for i in range(10001):
        length_list[i].sort()
        length_list_reverse[i].sort()

    for check in queries:
        if check[0] != "?":
            res = count_by_range(length_list[len(check)], check.replace('?','a'), check.replace('?','z'))
        else:
            res = count_by_range(length_list_reverse[len(check)], check[::-1].replace('?','a'), check[::-1].replace('?','z'))
        answer.append(res)

    # for check in queries:
    #     count = 0
    #     if check[0] == "?":
    #         for find_out in length_list[len(check)]:
    #             if find_out >= check[::-1].replace("?","a") and find_out <= check[::-1].replace("?","z"):
    #                 count += 1
    #     else:
    #         for find_out in length_list[len(check)]:
    #             if find_out >= check.replace("?","a") and find_out <= check.replace("?","z"):
    #                 count += 1
    #     answer.append(count)

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
                   ["fro??", "????o", "fr???", "fro???", "pro?"]))


# 테스트 1 〉	통과 (3.88ms, 11.5MB)
# 테스트 2 〉	통과 (4.28ms, 11.3MB)
# 테스트 3 〉	통과 (6.05ms, 11.4MB)
# 테스트 4 〉	통과 (3.82ms, 11.5MB)
# 테스트 5 〉	통과 (3.94ms, 11.5MB)
# 테스트 6 〉	통과 (4.46ms, 11.4MB)
# 테스트 7 〉	통과 (4.10ms, 11.4MB)
# 테스트 8 〉	통과 (4.32ms, 11.4MB)
# 테스트 9 〉	통과 (4.76ms, 11.3MB)
# 테스트 10 〉	통과 (4.20ms, 11.4MB)
# 테스트 11 〉	통과 (3.95ms, 11.4MB)
# 테스트 12 〉	통과 (3.90ms, 11.3MB)
# 테스트 13 〉	통과 (5.92ms, 11.7MB)
# 테스트 14 〉	통과 (5.38ms, 11.8MB)
# 테스트 15 〉	통과 (7.02ms, 11.5MB)
# 테스트 16 〉	통과 (5.83ms, 11.5MB)
# 테스트 17 〉	통과 (5.57ms, 11.7MB)
# 테스트 18 〉	통과 (5.66ms, 11.6MB)
# 효율성  테스트
# 테스트 1 〉	통과 (110.96ms, 24.4MB)
# 테스트 2 〉	통과 (145.68ms, 27.2MB)
# 테스트 3 〉	통과 (145.21ms, 29.2MB)
# 테스트 4 〉	통과 (6.50ms, 14MB)
# 테스트 5 〉	통과 (6.21ms, 14.4MB)


### trie 구조 학습 필요~