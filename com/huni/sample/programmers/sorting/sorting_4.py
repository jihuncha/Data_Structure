# https://programmers.co.kr/learn/courses/30/lessons/42747

# H-Index

# H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.
#
# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.
#
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
# 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

# 입출력 예
# citations	return
# [3, 0, 6, 1, 5]	3

# 입출력 예 설명
# 이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.
#
# ※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.



#########################################
# 문제가 이해가 안됨????
# 왜 filter로 해도 안되는거지? // index인경우는 왜??
# https://www.ibric.org/myboard/read.php?Board=news&id=270333
# 나의 h는 어떻게 구할 수 있을까? 우측의 표와 같이 자신이 저널에 등재한 전체 논문중 많이 인용된 순으로 정렬한 후,
# 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자가 바로 나의 h가 됩니다.
#########################################

def solution(citations):
    # temp_list = sorted(citations)
    #
    # for check in range(len(temp_list)):
    #     if temp_list[check] >= len(temp_list) - check:
    #         return len(temp_list) - check
    #
    # return 0

    temp_list = sorted(citations, reverse=True)

    # check -> 0,1,2,3,4,5... ???????뭐냐대체
    # temp_list[check] -> 인용한수
    for check in range(len(temp_list)):
        print("test - ", temp_list[check], check)
        if temp_list[check] <= check:
            return check

    return len(temp_list)

    # sorted_citations = sorted(citations, reverse=True)
    # for i in range(len(sorted_citations)):
    #     if sorted_citations[i] <= i:
    #         return i
    # return len(sorted_citations)

    # # print(temp_list)
    #
    # result_list = []
    # for idx,i in enumerate(temp_list):
    #     len_condition = len(list(filter(lambda x : x >= i, temp_list)))
    #     if len_condition >= i and len(temp_list) - len_condition <= i:
    #         if i not in result_list:
    #             result_list.append(i)
    #
    # # print(result_list)
    #
    # return max(result_list)


    # print("dd - ", list(filter(lambda x : x > 2, temp_list)))

    # count = 0
    # i = 0
    # result_list = []
    # while i < len(temp_list):
    #     count = temp_list[i]
    #     if len(list(filter(lambda x : x >= count, temp_list))) >= count and len(list(filter(lambda x : x < count, temp_list))) < count:
    #         # answer = count
    #         result_list.append(count)
    #     i += 1
    #
    # # print(result_list)
    # return max(result_list) if result_list else 0

print(solution([3, 0, 6, 1, 5]))
print(solution([3, 0, 6, 1, 5, 10]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 0, 0, 0]))
print(solution([6, 5, 4, 3, 1]))
print(solution([1]))