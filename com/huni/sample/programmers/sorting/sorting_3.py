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

def solution(numbers):
    answer = ''

    max_length = len(str(max(numbers)))
    # print(max_length)
    # int(str(x) + (str(x)[0] * (same_max_len - len(str(x
    temp = sorted(numbers, key=lambda x: int(str(x) + (str(x)[0] * (max_length - len(str(x))))) if len(str(x)) < max_length else int(str(x)), reverse=True)
    # print(temp)

    for result in temp:
        answer += str(result)


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