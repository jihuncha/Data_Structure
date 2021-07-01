import math

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