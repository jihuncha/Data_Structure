# def solution(board, skill):
#     answer = 0

#     for check in skill:
#         # print(check)
#         for i in range(check[1], check[3] + 1):
#             for j in range(check[2], check[4] + 1):
#                 if check[0] == 1:
#                     board[i][j] -= check[5]
#                 else:
#                     board[i][j] += check[5]
#         # print(board)
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] > 0:
#                 answer += 1


#     return answer

def solution(board, skill):
    answer = 0

    dic = {}

    # 문제 조건 상 -할 경우가 없는 경우는 계산 필요없이 전체다
    temp = [x for x in skill if x[0] == 1]
    if len(temp) == 0:
        return len(board) * len(board[0])

    for check in skill:
        # print(check)
        for i in range(check[1], check[3] + 1):
            for j in range(check[2], check[4] + 1):
                if (i, j) not in dic:
                    if check[0] == 1:
                        dic[(i, j)] = -check[5]
                    else:
                        dic[(i, j)] = check[5]
                else:
                    if check[0] == 1:
                        dic[(i, j)] -= check[5]
                    else:
                        dic[(i, j)] += check[5]
    # print(dic)

    for i in dic.keys():
        board[i[0]][i[1]] += dic[i]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    # print(board)

    return answer