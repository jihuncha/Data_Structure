

def recursive_test(a, b):
    def func_1(a, b):
        if a >= 10:
            return 100
        return recursive_test(a + 1, b)

    def func_2(a, b):
        if b >= 10:
            return 100
        return recursive_test(a, b + 1)
    # print(num)

    print(a,b)

    temp_1 = func_1(a,b)
    # temp_2 = func_2(a,b)

    # print("dsada", temp_1, temp_2)

    if temp_1 == 100:
        return 100

    # if temp_1 == 100 and temp_2 == 100:

    # print(temp_1, temp_2)



    # if num == 10:
    #     return -1
    #
    # temp = recursive_test(num + 1)

    # print("test" , temp)


    # return temp + 20

# def func_1(a,b):
#     if a == 10:
#         return 100
#     return recursive_test(a+1,b)
#
# def func_2(a,b):
#     if b == 10:
#         return 100
#     return recursive_test(a, b+1)

print(recursive_test(0,0))