# https://programmers.co.kr/learn/courses/30/lessons/42860

# 조이스틱

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

# def solution(name):
#     all_count = []
#
#     char_list = list(name)
#     visited = [[False] for _ in range(len(char_list))]
#
#     # print(visited)
#
#     def recursive_charator(count, i, visited_check):
#         num_count = ord(char_list[i]) - ord("A")
#
#         if num_count > 13:
#             num_count = 26 - num_count
#
#         count += num_count
#
#         i_plus = i + 1
#         if i_plus > len(char_list) - 1:
#             i_plus = 0
#
#         i_minus = i - 1
#         if i_minus < 0:
#             i_minus = len(char_list) - 1
#         # print(i_minus)
#
#         visited_check[i] = True
#
#         # if visited_check[i]:
#         #     recursive_charator(count + 1, i_plus, visited_check)
#         #     recursive_charator(count + 1, i_minus, visited_check)
#         #     return
#
#         if [False] not in visited_check:
#             all_count.append(count)
#             return
#
#         recursive_charator(count + 1, i_plus, visited_check)
#         recursive_charator(count + 1, i_minus, visited_check)
#
#     recursive_charator(0, 0, visited)
#     print(all_count)



    # i = 0
    # while [False] in visited:
    #     visited[i] = True
    #     print(i, visited)
    #     i += 1

    # def recursive_charactor(count, char):
    #     num_count = ord(char) - ord("A")
    #
    #     if num_count > 13:
    #         num_count = 26 - num_count
    #
    #     count += num_count
    #

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
# print(solution("ZZAAAZZ"))


### 다른 사람 풀이 1.

def solution(name):
    cnt = 0  # 총 이동 횟수
    a_cnt = 0  # 'A'의 개수
    a_max = 0  # 'A'의 최대개수
    idx = 0  # 최대'A'개수 문자열의 마지막 인덱스
    a_startIdx = 0  # 최대'A'개수 문자열의 첫번째 인덱스
    wander_cnt = 0  # 좌우로 왔다갔다하는 횟수 카운트

    # 위, 아래 조이스틱 계산
    for i, n in enumerate(name):
        if n == 'A':  # 'A'개수의 최대값과 그 인덱스 계산
            a_cnt += 1
            if a_cnt > a_max:
                a_max = a_cnt
                idx = i
        else:
            cnt += min(ord(n) - ord('A'), ord('Z') - ord(n) + 1)
            a_cnt = 0

    # 최대'A'개수의 시작 인덱스
    a_startIdx = idx - a_max + 1

    # 최대'A'가 맨 앞이나 맨 끝에 있는 경우
    if a_startIdx == 0 or idx == len(name) - 1:
        cnt += len(name) - 1 - a_max  # a_max개만큼 이동 안해도 됨
    else:
        left = len(name) - idx - 1  # 최대'A'뒤에 남아있는 문자의 개수
        if a_startIdx <= left:  # 뒤에 문자가 앞에 문자개수보다 많은 경우
            wander_cnt = (a_startIdx - 1) * 2 + left
        else:
            wander_cnt = (a_startIdx - 1) + left * 2
        cnt += min(wander_cnt, len(name) - 1)  # 그냥 한쪽방향으로 모두 이동하는 것과 비교

    return cnt

print(solution("ZZAAAZZ"))

### 다른 사람 풀이 2.

def solution(name):
    make_name = [min(ord(i) - ord("A"), ord("Z") - ord(i)+1) for i in name]
    print(make_name)
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]

        print("count - ", make_name[idx])

        make_name[idx] = 0
        if sum(make_name) == 0:
            break

        left, right = 1, 1
        # ??? 모하는놈이지..
        # 왼쪽 / 오른쪽이 A가 아닌 경우의수까지 이동??인듯
        while make_name[idx - left] == 0:
            left +=1
        while make_name[idx + right] == 0:
            right +=1

        # 짧은 쪽으로 이동
        print(left, right)
        answer += left if left < right else right
        print(answer)
        idx += -left if left < right else right
    return answer

print(solution("ZZAAAZAAZ"))