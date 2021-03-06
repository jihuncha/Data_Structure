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

####################################################################################################
# 미해결 but 생각 공유
# 1. Combination 써서 모든 경우의 수 구하면 바로 해결될줄 알았으나 어김없이 time out
# 2. while 이용한 전체 순회인데...아마 너무 긴 숫자가 안되는듯 (8,10 (타임아웃 2개)) -> 여기서 시간 줄여볼려다가 포기
#
####################################################################################################


# combination 으로는 timeout이 떨어진다.
def solution(number, k):
    # 1. combination 답 - timeout

    # temp_list = sorted([int(''.join(x)) for x in itertools.combinations(list(number), len(number) - k)], reverse=True)
    #
    # return str(max(temp_list))

    # return str(temp_list[0])

    # 2. 다른 풀이
    # while 이용한 전체 순회인데...아마 너무 긴 숫자가 안되는 모양
    # 8,10 (타임아웃 2개)
    # not_end = False
    # count = 0
    # temp_list = list(number)
    #
    # idx = 0
    # while count != k:
    #     # 모든 순환을 한 경우
    #     if idx + 1 > len(temp_list) - 1:
    #         not_end = True
    #         break
    #
    #     if int(temp_list[idx]) < int(temp_list[idx + 1]):
    #         temp_list.pop(idx)
    #         count +=1
    #         idx = 0
    #     else:
    #         idx += 1
    #
    # if not_end:
    #     for i in range(k - count):
    #         temp_list.pop()
    #
    # return ''.join(temp_list)

    # 3. 다른 풀이 3 - 하여간 천재들 많네..
    stack = []
    my_num = list(number)
    stack.append(my_num[0])

    for idx,num in enumerate(number[1:]):
        # 맨앞에 수보다 작은 경우 ? 제거해준다
        # 전체 순회하면서
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
        print(stack, k)

    # 전체 순회했는데 뒤에 숫자가 더 큰 경우는 앞에서 부터 제거
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution("233333334",5))

# "4177252841" 4	"775841"