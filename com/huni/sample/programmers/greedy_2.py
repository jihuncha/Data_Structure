# https://programmers.co.kr/learn/courses/30/lessons/42860

# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA
#
# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
#
# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
#
# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다. - ???
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# name	return
# "JEROEN"	56
# "JAN"	23

# 26 개
# abcdefghijklmnopqrstuvwxyz
# 13 이상이면 26 - x 로 표현하면될듯

# 이 문제의 문제는 중간에 A의 요소...
# JAAAABAACAA
# JAABAACAAAB
# JBAAAZ

# JAABAAABAAB
# JAAAAAAZ

# 둘다 카운트 갯수는 최소 카운트 횟수는 동일 / 양쪽 방향 탐색해서 A의 길이를 파악해야되나 ?


# 이거 그냥 앞으로 한번 뒤로 한번 하면 되지않을까??
# 첫번쨰 것만 먼저 실행하고 나머지 문자열은 순서대로 진행하면될듯????
# 알파벳 길이가 3이상인 경우만 2가지 실행해준다.

# ZZAAAZZ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ

def solution(name):
    # a,b = 0,0
    #
    # # 문자열 list 생성
    # my_list = list(name)
    # my_reverse = list(my_list[0]) + my_list[-1:0:-1]
    # # print(my_reverse)
    #
    # for idx,i in enumerate(my_list):
    #     num_count = ord(i) - ord("A")
    #
    #     if num_count == 0:
    #         # 나머지가 전부 a인경우는 빠져 나간다.
    #         if set(my_list[idx:len(my_list)]) == set('A'):
    #             break
    #
    #         # 아닌 경우 다음 칸으로 이동 (카운트 더해서)
    #         a += 1
    #         continue
    #
    #     if num_count > 13:
    #         num_count = 26 - num_count
    #
    #     a += num_count + 1
    #
    # if len(my_list) >= 3:
    #     for idx, i in enumerate(my_reverse):
    #         num_count = ord(i) - ord("A")
    #
    #         # print(i, num_count)
    #
    #         if num_count == 0:
    #             # 나머지가 전부 a인경우는 빠져 나간다.
    #             if set(my_reverse[idx:len(my_reverse)]) == set('A'):
    #                 break
    #
    #             # 아닌 경우 다음 칸으로 이동 (카운트 더해서)
    #             b += 1
    #             continue
    #
    #         if num_count > 13:
    #             num_count = 26 - num_count
    #
    #         b += num_count + 1
    #
    # if len(my_list) >= 3 and b != 0:
    #     return min(a-1, b-1)
    # else:
    #     return a-1
# print(solution("ZZZ"))
print(solution("ZZAAAZZ"))