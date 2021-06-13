# 이진 탐색

# for문 이용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


# 원소의 개수 / target
n, target = list(map(int, input().split()))

# 전체 원소
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 읎다")
else:
    print(result + 1)

# 입력
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# 출력
# 4