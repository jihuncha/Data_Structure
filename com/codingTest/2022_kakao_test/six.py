# board	skill	result
# [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]	10
# [[1,2,3],[4,5,6],[7,8,9]]	[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	6

def solution(board, skill):
    minus_list = [x for x in skill if x[0] == 1]
    plus_list = [x for x in skill if x[0] == 2]

    if len(minus_list) == 0:
        return len(board) * len(board[0])

    count_dic = {}

    for minus in minus_list:
        for i in range(minus[1], minus[3] + 1):
            for j in range(minus[2], minus[4] + 1):
                board[i][j] -= minus[5]
                if board[i][j] <= 0:
                    count_dic[(i,j)] = board[i][j]

    if not count_dic:
        return len(board) * len(board[0])

    for plus in plus_list:
        for i in range(plus[1], plus[3] + 1):
            for j in range(plus[2], plus[4] + 1):
                if not count_dic:
                    break
                if (i,j) in count_dic:
                    count_dic[(i,j)] += plus[5]
                    if count_dic[(i,j)] > 0:
                        del count_dic[(i,j)]

    return len(board) * len(board[0]) - len(count_dic.keys())

    # print(skill)
    #
    # for check in skill:
    #     # print(check)
    #     for i in range(check[1], check[3] + 1):
    #         for j in range(check[2], check[4] + 1):
    #             if (i,j) not in dic:
    #                 if check[0] == 1:
    #                     dic[(i,j)] = -check[5]
    #                 else:
    #                     dic[(i, j)] = check[5]
    #             else:
    #                 if check[0] == 1:
    #                     dic[(i,j)] -= check[5]
    #                 else:
    #                     dic[(i, j)] += check[5]
    # print(dic)
    #
    # for i in dic.keys():
    #     board[i[0]][i[1]] += dic[i]
    #
    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if board[i][j] > 0:
    #             answer += 1

    # print(board)

    # return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))