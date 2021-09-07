import math
import bisect

arr = [1, 4, 6, 8, 3, 5, 6, 7]

# 염두할 것은 Sequence arr 의 0 번째 인덱스에 음의 무한을 넣었다는 것.
# 이것은 [100, 1, 2, 3]과 같이 원 Sequence의 첫 번째 값이 가장 큰 값일 때를 대비하기 위한 것.

def lis(arr):
    arr = [-math.inf] + arr
    N = len(arr)
    cache = [-1] * N

    def find(start):
        if cache[start] != -1:
            return cache[start]

        ret = 0
        for nxt in range(start+1, N):
            if arr[start] < arr[nxt]:
                ret = max(ret, find(nxt) + 1)

        cache[start] = ret
        return ret

    return find(0)

print(lis(arr))
print("##########################################################################")
##################################################################

# 1. dp 방식
dp_table = [1 for _ in range(len(arr))]
# print(dp_table)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)
print(dp_table)

print("##########################################################################")
# 2. binary search 방식 -> 굳이 이전걸 전부 체크할필요가 없으므로..
# 1. dp를 arr[0]으로 초기화한다.
# 2. 현재 위치(i)가 이전 위치의 원소들보다 크면 dp에 추가한다.
# 3. 현재 위치(i)가 이전 위치의 원소보다 작거나 같으면, bisect.bisect_left로 이전 위치의 원소 중 가장 큰 원소의 index값을 구한다. 그리고 dp의 index 원소를 arr[i]로 바꿔준다.

dp_table = [arr[0]]

for i in range(len(arr)):
    if arr[i] > dp_table[-1]:
        dp_table.append(arr[i])
    else:
        idx = bisect.bisect_left(dp_table, arr[i])
        dp_table[idx] = arr[i]

print(dp_table)
print(len(dp_table))

print("##########################################################################")
# 가장 긴 증가하는 부분 수열을 직접 구할 때
# LIS의 길이뿐만 아니라 LIS 원소들을 알고 싶으면 어떻게 해야 할까?

# 1. dp 방식
dp_table = [1 for _ in range(len(arr))]
# print(dp_table)

for i in range(len(arr)):
    for j in range(i):
        if arr[i] > arr[j]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)
print(dp_table)

max_dp = max(dp_table)
print(max_dp)

max_idx = dp_table.index(max_dp)
lis = []

while max_idx >= 0:
    if dp_table[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()
print(lis)
