# This is a demo task.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Copyright 2009–2021 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

A = [1, 3, 6, 4, 1, 2]

A = [1,2,3]

# A = [-1, -3]


def solution(A):
    # write your code in Python 3.6

    f = list(filter(lambda a:a>0, A))
    # print(f)

    if len(f) == 0:
        return 1

    f.sort()
    # print(f)

    temp = [x+1 for x in range(len(f))]
    # print(temp)

    f = list(set(f))

    if (f[:] == temp[:]):
        return f[-1] + 1

    for i in range(1,len(f) + 1):
        if f[i-1] != i:
            return i



    # temp = [x+1 for x in range(len(A))]
    # print(temp)

    # result_list = list(set(A))
    # # print(result_list)
    #
    # for i in range(len(result_list)):
    #     # print(temp[i], result_list[i])
    #     if temp[i] != result_list[i]:
    #         return temp[i]
    #
    # if len(temp) == len(result_list):
    #     return temp[-1] + 1
    #
    # return temp[len(result_list)]

    pass

print(solution(A))

