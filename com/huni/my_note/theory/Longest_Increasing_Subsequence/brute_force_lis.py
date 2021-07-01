arr = [1, 4, 6, 8, 3, 5, 6, 7]

def lis(arr):
    if not arr:
        return 0

    ret = 1
    for i in range(len(arr)):
        nxt = []
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret

print(lis(arr))

