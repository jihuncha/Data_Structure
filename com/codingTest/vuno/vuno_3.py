# 여집합 구하는 문제인듯

# 3
# 2 1 2 5 6
# 1 1 3
# 1 4 10

# 1

# 3
# 2 1 3 6 7
# 1 2 4
# 2 2 5 9 12

# 2

n = int(input())

# 모든값을 담아줄 set선언
temp_set = set()

for i in range(n):
    temp = list(map(int, input().split()))
    # list에서 뽑아내야할 아이들 count
    count = temp[0]
    # 해당 list들
    check_list = temp[1:]
    # 2칸씩 진행
    for i in range(0, count + 1, 2):
        # 시작과 끝의 list (끝을 포함안하는게맞는가..? 여기서 잘 이해가...)
        start_end_list = [x for x in range(check_list[i], check_list[i+1])]
        # 다시 추출하여 set에 담아준다.
        for j in range(len(start_end_list)):
            temp_set.add(start_end_list[j])

# set을 list형태로 다시 변환
check = list(temp_set)
# count를 담아줄 변수
count = 0

for i in range(len(check) - 1):
    # 다음값이 1이상인 경우는 count 올려준다..
    if check[i] + 1 != check[i+1]:
        count +=1

print(count)

        # start_end = [check_list[i], check_list[i+1]]
        # print(start_end)

        # temp_list.append(start_end)

#         for j in result:
#             temp_set.add(j)
#         # print(result)
#         # temp_set.union(set(x for x in range(check_list[i], check_list[i+1] + 1)))
#
# print(list(temp_set))
#
# check = list(temp_set)
# count = 0
# for i in range(len(check) - 1):
#     if check[i] + 1 != check[i+1]:
#         count +=1
#
# print(count)



