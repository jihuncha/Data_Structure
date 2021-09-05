# 고정점 찾기

# 5
# -15 -6 1 3 7
#
# 3
#
# 7
# -15 -4 2 8 9 13 15
#
# 2
#
# 7
# -15 -4 3 8 9 13
#
# -1

n = int(input())

data = list(map(int, input().split()))

# mid = (data[0] + data[len(data) - 1]) // 2
# print(mid)

start = 0
end = len(data) - 1
# print(start,end)

result = -1

while start <= end:
    # print("dsa")
    mid = (start + end) // 2
    print(mid)

    if data[mid] == mid:
        result = mid
        break

    if data[mid] < mid:
        start = mid + 1
        print("start - ", start, end)
    else:
        end = mid - 1
print(result)

