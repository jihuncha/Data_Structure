array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array, start, end):
#     if start >= end: #원소가 한 개인 경우 종료
#         return
#
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         # 피벗보다 큰 데이터를 찾을 때 까지 반복
#         while left <= end and array[left] <= array[pivot]:
#             left+=1
#         # 피벗보다 작은 데이터를 찾을 때 까지 반복
#         while right > start and array[right] >= array[pivot]:
#             right -= 1
#         if left > right:
#             array[right], array[pivot] = array[pivot], array[right]
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     quick_sort(array, start, right-1)
#     quick_sort(array, right+1, end)
#
# quick_sort(array, 0, len(array) -1)
# print(array) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#python style
def quick_sort(array):
    # 1개 이하일 경우 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] #작은 애들은 왼쪽
    right_side = [x for x in tail if x > pivot] #큰 애들은 오른쪽
    # print("left - ", left_side)
    # print("right -", right_side)
    # print("pivot - ", pivot)
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
