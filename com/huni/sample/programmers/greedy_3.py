# https://programmers.co.kr/learn/courses/30/lessons/42883

# 큰 수 만들기

# 문제 설명
# 어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.
#
# 예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.
#
# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다.
#
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
# k는 1 이상 number의 자릿수 미만인 자연수입니다.

# number	k	return
# "1924"	2	"94"
# "1231234"	3	"3234"
# "4177252841" 4	"775841"
# "2134" 3     "4"
import itertools


# combination 으로는 timeout이 떨어진다.
def solution(number, k):
    # 1. combination 답 - timeout
    # temp_list = sorted([int(''.join(x)) for x in itertools.combinations(list(number), len(number) - k)], reverse=True)
    #
    # return str(max(temp_list))

    # return str(temp_list[0])

    # 2. 다른 풀이
    # 8,10 (타임아웃 2개)
    not_end = False
    count = 0
    temp_list = list(number)

    idx = 0
    while count != k:
        # 모든 순환을 한 경우
        if idx + 1 > len(temp_list) - 1:
            not_end = True
            break

        if int(temp_list[idx]) < int(temp_list[idx + 1]):
            temp_list.pop(idx)
            count +=1
            idx = 0
        else:
            idx += 1

    if not_end:
        for i in range(k - count):
            temp_list.pop()

    return ''.join(temp_list)

print(solution("4321",3))

# "4177252841" 4	"775841"