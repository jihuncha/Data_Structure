# info	edges	result
# [0,0,1,1,1,0,1,0,1,0,1,1]	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]	5
# [0,1,0,1,1,0,1,0,0,1,0]	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	5

# def dfs(start:list, count_lamb:int,data:list):
#     stack = start
#
#     while stack:
#         temp = stack.pop()
#         for i in data[temp]:
#             if info[]


def solution(info, edges):
    answer = 0

    data = [[]  for _ in range(len(edges))]
    # print(data)

    for i in edges:
        data[i[0]].append(i[1])
    print((data))
    print((info))

    stack = [0]
    lamb_count = 1

    visited = [False] * len(info)

    while stack:
        temp = stack.pop()
        for i in data[temp]:
            if not visited[i]:
                visited[i] = True
                if info[i] == 0:
                    lamb_count +=1
                else:
                    lamb_count -= 1

                if lamb_count == 0:
                    break
            else:
                continue

    print(visited)
    print(lamb_count)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],	[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
