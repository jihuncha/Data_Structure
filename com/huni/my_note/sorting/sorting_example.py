

# 선택 정렬 예시
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
#
# print(array)

# 삽입 정렬 예시
for i in range(1, len(array)):
    for j in range(i, 0, -1): #인덱스 i 부터 0까지 감소하면서 탐색
        # print(j)
        if array[j] < array[j - 1]: #한 칸 씩 왼쪽으로
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            # 자기보다 작은 데이터를 만나면 그 자리에서 멈춘다.
            break

print(array)
