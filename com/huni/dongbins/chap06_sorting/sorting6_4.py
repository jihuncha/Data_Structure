# 두 배열의 원소 교체

# input
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
#
# output
# 26

n,k = map(int,input().split())

list_a = list(map(int,input().split()))
list_b = list(map(int,input().split()))

print(list_a)
print(list_b)

list_a.sort()
list_b.sort(reverse=True)

for i in range(k):
    if list_a[i] < list_b[i]:
        list_a[i], list_b[i] =list_b[i], list_a[i]
    else:
        break

print(sum(list_a))