def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result


# 재귀 이용
def factorial_recursive(n):
    if n <= 1:
        return 1

    return n * factorial_iterative(n - 1)


print(factorial_iterative(5))   #120
print(factorial_recursive(5))   #120