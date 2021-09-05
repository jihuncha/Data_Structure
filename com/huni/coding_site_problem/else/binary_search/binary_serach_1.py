# 정렬된 배열에서 특정 수 구하기

# 7 2
# 1 1 2 2 2 2 3

# 4

# 7 4
# 1 1 2 2 2 2 3
# -1

import bisect

n,target = map(int, input().split())

data = list(map(int,input().split()))

def count_by_range(x:int):
    left_index = bisect.bisect_left(data, x)
    right_index =bisect.bisect_right(data, x)
    return right_index - left_index

result = count_by_range(target)

print(result if result !=0 else -1)
