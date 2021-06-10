# 부품 찾기

# N 개의 부품이 있다 -> 손님이 M개의 종류의 부품을 대량으로 구매하겠다고 견적서 요청
#
# N = 5
# [8, 3, 7, 9, 2]
#
# 3개의 부품이 있는지 요청
# [5, 7, 9]
#
# 손님이 요청한 부품 번호의 순서대로 부품을 확인해 있으면 yes, 없으면 no를 출력
#
# * 조건
# 1. 첫째줄에 정수 N (1<= n <= 1000000)
# 2. 둘째 줄에 공백으로 N개의 정수 가 주어짐 (1보다크고 1000000 이하)
# 3. 셋째 줄에 정수 M (1<= m <= 100000)
# 4. 넷째줄에 M개의 정수 (1보다크고 1000000 이하)
#
# * 출력
# 부품이 있으면 yes, 없으면 no

# * 입력예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9
#
# 출력 예시
# no yes yes

from typing import List
import sys

def binary_search_recursive(array:List, target:int, start:int, end:int):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid + 1
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid+1, end)
    else:
        return binary_search_recursive(array, target, start, mid-1)

n = int(sys.stdin.readline().rstrip())

array = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

target_list = list(map(int, sys.stdin.readline().rstrip().split()))

for target in target_list:
    if binary_search_recursive(array, target, 0, n - 1) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')
        

# 이진 탐색이 아닌 계수 정렬로도 가능하다!!
n = int(input())
array = [0] * 1000001

# 부품 번호 입력
for i in input().split():
    array[int(i)] = 1
    
m = int(input())

x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print("yes", end=' ')
    else:
        print("no", end=' ')

# 또한 집합 자료형 이용해서 가능
n = int(input())
array = set(map(int, input().split()))

m = int(input())

x = list(map(int, input().split()))

for i in x:
    if i in array:
        print("yes", end=' ')
    else:
        print("no", end=' ')


