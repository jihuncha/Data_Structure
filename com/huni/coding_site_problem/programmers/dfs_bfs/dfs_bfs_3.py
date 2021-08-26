# https://programmers.co.kr/learn/courses/30/lessons/43163

# 단어 변환

# 문제 설명
# 두 개의 단어 begin, target과 단어의 집합 words가 있습니다. 아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
#
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
# 2. words에 있는 단어로만 변환할 수 있습니다.
# 예를 들어 begin이 "hit", target가 "cog", words가 ["hot","dot","dog","lot","log","cog"]라면 "hit" -> "hot" -> "dot" -> "dog" -> "cog"와 같이 4단계를 거쳐 변환할 수 있습니다.
#
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 각 단어는 알파벳 소문자로만 이루어져 있습니다.
# 각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
# words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
# begin과 target은 같지 않습니다.
# 변환할 수 없는 경우에는 0를 return 합니다.
# 입출력 예
# begin	target	words	return
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
# "hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	0
# 입출력 예 설명
# 예제 #1
# 문제에 나온 예와 같습니다.
#
# 예제 #2
# target인 "cog"는 words 안에 없기 때문에 변환할 수 없습니다.

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    stack = [begin]
    visited = [False] * len(words)
    # print(visited)

    while stack:
        temp = stack.pop()

        if temp == target:
            return answer

        for check in range(len(words)):
            if visited[check]:
                continue

            count = 0
            for a,b in zip(temp, words[check]):
                if a != b:
                    count += 1

            if count == 1:
                # print(visited)
                visited[check] = True
                stack.append(words[check])
        print(visited)
        answer += 1

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


### 아무리해도안되넹


# def dfs(word, words_list: list, visited, temp_result, target):
#     if word == target:
#         answer_list.append(temp_result)
#         return
#
#     for i in range(len(words_list)):
#         if visited[i]:
#             continue
#
#         temp = 0
#         for j in range(len(words_list[i])):
#             if words_list[i][j] != word[j]:
#                 temp += 1
#
#         if temp == 1:
#             temp_result += 1
#             visited[i] = True
#             # print(words_list[i], words_list, visited, temp_result)
#             dfs(words_list[i], words_list, visited, temp_result, target)
#             visited[i] = False
#
# def solution(begin, target, words):
#     global answer_list
#     answer = 0
#
#     if target not in words:
#         return answer
#
#     visited = [False] * (len(words))
#     answer_list = []
#
#     dfs(begin, words, visited, 0,target)
#
#     # print(answer_list)
#
#     return min(answer_list) if len(answer_list) != 0 else 0


    # result_list = []
    # for i in range(len(begin)):
    #     temp = begin[:i] + '0' + begin[i+1:]
    #     result_list.append(temp)


    # start_str = begin
    # temp_str = [''.join(list(x)) for x in list(combinations(start_str, len(begin) - 1))]
    # print(temp_str)
    #
    # for i in temp_str:
    #     for j in words:
    #         if set(i).issubset(set(j)):
    #             print("?")

        # print(my_str)

# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))

# 테스트 1 〉	실패 (0.01ms, 10.4MB)
# 테스트 2 〉	실패 (0.03ms, 10.2MB)
# 테스트 3 〉	실패 (0.07ms, 10.3MB)
# 테스트 4 〉	실패 (0.01ms, 10.3MB)
# 테스트 5 〉	통과 (0.00ms, 10.3MB)

# test = 'abc'
# test_2 = 'ac'
#
# if test_2 in test:
#     print("s")

# answer = 0
def dfs(begin, target, words, visited):
    global answer
    stacks = [begin]

    while stacks:
        # 스택을 활용한 dfs 구현
        stack = stacks.pop()

        if stack == target:
            return answer

        for w in range(0, len(words)):
            # 조건 1. 한 개의 알파벳만 다른 경우
            if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:
                if visited[w] != 0:
                    continue

                visited[w] = 1
                # stack에 추가
                stacks.append(words[w])
        # depth +
        answer += 1

def solution(begin, target, words):
    global answer
    answer = 0

    # 조건 2. words에 있는 단어로만 변환할 수 있습니다.
    if target not in words:
        return 0

    visited = [0 for i in words]
    print(visited)

    dfs(begin, target, words, visited)
    # stacks = [begin]

    # while stacks:
    #     # 스택을 활용한 dfs 구현
    #     stack = stacks.pop()
    #
    #     if stack == target:
    #         return answer
    #
    #     for w in range(0, len(words)):
    #         # 조건 1. 한 개의 알파벳만 다른 경우
    #         if len([i for i in range(0, len(words[w])) if words[w][i] != stack[i]]) == 1:
    #             if visited[w] != 0:
    #                 continue
    #
    #             visited[w] = 1
    #             # stack에 추가
    #             stacks.append(words[w])
    #     # depth +
    #     answer += 1

    return answer

# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))
