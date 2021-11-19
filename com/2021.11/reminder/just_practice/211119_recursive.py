

def recursive_test(num:int):
    print(num)

    if num == 10:
        return -1

    temp = recursive_test(num + 1)

    print("test" , temp)


    return temp + 20


print(recursive_test(0))