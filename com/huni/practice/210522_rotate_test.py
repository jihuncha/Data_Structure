

my_list = [[1,2,3],[4,5,6],[7,8,9]]

print(len(my_list))
print(len(my_list[0]))

# 123
# 456
# 789
#
# 741
# 852
# 963
#
# 11 12 13
# 21 22 23
# 31 32 33
#
# 00 01 02
# 10 11 12
# 20 21 22
#
# 00 -> 02 -> 22 -> 20
# 01 -> 12 -> 21 -> 10
# 02 -> 22 -> 20 -> 00
#
# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33
#
# 00 -> 03 -> 33 -> 30
# 01 -> 13 -> 32 -> 20
# 02 -> 23 -> 31 -> 10
# 03 -> 33 -> 30 -> 00


# print(my_list[0][0])

def rotate():
    result_list = [[0] * len(my_list[0]) for _ in range(len(my_list))]
    # 열의수
    for i in range(0, len(my_list)):
        #행의수
        for j in range(0, len(my_list[0])):
            # print("d")
            # print(j,i)
            # print("test - ",i,j)
            # print("test2", my_list[i][j])
            # print(i, 3 - j - 1)
            result_list[j][len(my_list)-i-1] = my_list[i][j]
            # my_list[i][i] = my_list[i][3 - j  - 1]

    return result_list

print(rotate())

print(my_list)
# print()