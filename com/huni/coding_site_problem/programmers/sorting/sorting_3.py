# https://programmers.co.kr/learn/courses/30/lessons/42746

# 가장 큰 수

# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

# 입출력 예
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"

#########################################
# 포기...
# 처음에 큰 수의 정렬이 잘 안됬음.. [3, 30, 34, 333335, 9]
# sorted로 자리수가 가장 긴 길이 가져와서 짧은 길이의 애들은 맨앞과 동일 숫자로 정렬하였으나 실패 ([898,89])
# 그 다음은 sum으로 해결하려 했으나 실패....
# quicksort로 푸는 사람도 있었음
#########################################

def solution(numbers):
    answer = ''

    # 1. sort 활용
    max_length = len(str(max(numbers)))

    # if (len(numbers) <=)
    numbers = list(map(str, numbers))
    # temp = sorted(numbers, key=lambda x: (str(x) + (str(x)[0] * (max_length - len(str(x)))) if len(str(x)) < max_length else str(x)), reverse=True)
    temp = sorted(numbers, key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(temp)))

    # for result in temp:
    #     if result == 0:
    #         if len(answer) == 0:
    #             answer = '0'
    #     else:
    #         answer += str(result)
    #
    # 2.
    # temp = sorted(numbers, key=lambda x:int(str(x)[0]), reverse=True)
    #
    # temp_str = ''
    # for i in range(len(temp) - 1):
    #     if str(temp[i])[0] != str(temp[i + 1])[0]:
    #         if len(temp_str) > 0:
    #             answer += temp_str
    #             temp_str = ''
    #         answer += str(temp[i])
    #
    #     else:
    #         str_a = ''
    #         if len(temp_str) > 0:
    #             str_a = temp_str
    #         else:
    #             str_a = str(temp[i])
    #         str_b = str(temp[i + 1])
    #         result = max(int(str_b + str_a), int(str_a + str_b))
    #         temp_str = str(result)
    #
    # if len(temp_str) > 0:
    #     answer += temp_str
    # else:
    #     answer += str(temp[-1])



    # temp_str = str(temp[0])
    # same_list = []
    # same_max_len = 0
    #
    # for check in temp[1:]:
    #     check_str = str(check)
    #     if check_str[0] == temp_str[0]:
    #         if not same_list:
    #             same_list.append(temp_str)
    #         same_list.append(check_str)
    #         same_max_len = len(check_str) if len(check_str) > len(temp_str) else len(temp_str)
    #     else:
    #         if same_list:
    #             same_list.sort(key=lambda x: int(str(x) + (str(x)[0] * (same_max_len - len(str(x))))) if len(
    #                 str(x)) < same_max_len else int(str(x)))
    #             print(same_list)
    #             while same_list:
    #                 temp_str += same_list.pop()
    #             print(temp_str)
    #             # # print(same_list, same_max_len)
    #             # same_list.sort(key=lambda x: int(str(x)*same_max_len) if len(str(x)) < same_max_len else int(str(x)), reverse=True)
    #         answer += temp_str
    #     temp_str = str(check)
    #
    # if len(temp_str) != 0:
    #     answer += temp_str
    # # same_list.sort(key=lambda x: int(str(x) + (str(x)[0] * (same_max_len - len(str(x))))) if len(str(x)) < same_max_len else int(str(x)), reverse=True)
    # # print(same_list, same_max_len)
    #
    #
    #     # if check_str[0] == temp_str[0] and len(check_str) >= 2:
    #         # if len(temp_str) < len(check_str):
    #         #     change = temp_str + temp_str[0] * (len(check_str) - len(temp_str))
    #         # else:
    #         #     change = check_str + temp_str[0] * (len(temp_str) - len(check_str))
    #         # print(change)
    #         # same_str = same_str + check_str if int(change) <= int(check_str) else check_str + same_str
    #         # # temp_str = str(check)
    # # if len(same_str) > 0:
    # #     answer += same_str
    # # if temp_str:
    # #     answer += temp_str

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 30, 34, 333335, 9]))
print(solution([412,41]))
print(solution([303,30]))
print(solution([898,89]))
print(solution([0,0]))
print(solution([898,89,89898]))


#########################################

# 다른사람 풀이 1.
# 문제의 numbers의 원소는 0 이상 1,000 이하입니다. 라는 조건을 통해서 numbers.sort(key=lambda x" x*3, reverse = True)를 해서 정렬
# [6, 10, 2]을 예시로 들면, numbers.sort(key=lambda x" x*3, reverse = True)를 하면,
# [666, 101010, 222]가 되고 이를 정렬하면, [666, 222, 101010]이 되어서 결과적으로 [6, 2, 10]의 순서가 된다.
# 위와 같이 정렬되는 이유는 박상희님의 댓글에 따르면 "문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다.
# 물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다."
# 즉, 앞자리가 큰 6 -> 2 -> 1순으로 정렬되어서 위와 같은 결과를 얻게 된 것입니다.

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

# 다른사람 풀이 2.
# functools 체크
# functools.cmp_to_key(func)
# 구식 비교 함수를 키 함수로 변환합니다. (sorted(), min(), max(), heapq.nlargest(), heapq.nsmallest(), itertools.groupby()와 같은)
# 키 함수를 받아들이는 도구와 함께 사용됩니다.
# 이 함수는 주로 비교 함수 사용을 지원하는 파이썬 2에서 변환되는 프로그램의 전이 도구로 사용됩니다.
#
# 비교 함수는 두 개의 인자를 받아들이고, 그들을 비교하여, 작으면 음수, 같으면 0, 크면 양수를 반환하는 콜러블입니다.
# 키 함수는 하나의 인자를 받아들이고 정렬 키로 사용할 다른 값을 반환하는 콜러블입니다.
#
# 예:
#
# sorted(iterable, key=cmp_to_key(locale.strcoll))  # locale-aware sort order
# 정렬 예제와 간략한 정렬 자습서는 정렬 HOW TO를 참조하십시오.

# import functools
# 
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
# 
# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer

