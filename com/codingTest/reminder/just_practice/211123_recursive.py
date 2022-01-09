def A(input: int):
    # print(input)
    if input <= 0:
        return -1
    return A(input - 1)

def B(input: int):
    # print(input)
    if input >= 10:
        return 1
    return B(input + 1)

# print(A(10))
# print(B(10))


def test():
    a = A(10)
    b = B(1)

    if a+b == 0:
        return 0

    test()

print(test())