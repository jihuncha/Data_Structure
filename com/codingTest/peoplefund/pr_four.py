# k를 넘지 않는 숫자의 list중 가장 길이가 적은 list를 만들어라......

a = [2,3,3,7,3,5]
k = 20

# 결과 : 3

# a = [1,3,2,5,4]
# k = 6

# 3
def getMinLength(a, k):
    temp_list = sorted(a)

    if temp_list[0] * temp_list[1] > k:
        return len(a)

    current_index = 0
    while True:
        if current_index + 1 < len(a):
            temp_num = a[current_index] * a[current_index + 1]
            if temp_num <= k:
                a = a[:current_index] + [temp_num] + a[current_index+2:]
            else:
                current_index += 1
        else:
            break

    return len(a)


print(getMinLength(a,k))