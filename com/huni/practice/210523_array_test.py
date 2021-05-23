# array...
my_list = [[1,2,3],[4,5,6],[7,8,9]]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

# def check_all(my_list, x,y):

for i in range(4):
    x = dx[i]
    y = dy[i]

    result_list = [[0] * len(my_list) for _ in range(len(my_list))]

    # for i in
    # result_list[1][0] = my_list[0][0]


# def moving(my_list, x, y):
#     if

# print([1 in x for x in my_list])

# for i in range(my_list):
#     for j in range(my_list[0]):
#         if i + 1 > len(my_list) - 1:
#             my_list[]


a_list = [[1,2], [2,3]]
b_list = [[2,3], [1,2]]

print(sorted(a_list)[:] == sorted(b_list)[:])