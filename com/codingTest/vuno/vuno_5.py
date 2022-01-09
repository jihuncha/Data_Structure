# 숨바꼭질

# 50 100

# 1

# 5 17

# 4

n,k = map(int, input().split())

count = 0

# n과 k가 같지 않은 경우만 실행한다.
while n != k:
    # 문제 조건 - n이 이미 더 큰 경우는 계속 감산한다.
    if n > k:
        count += n - k
        break

    # 2배를 했을때 해당위치의 경우는 빠져나가면된다.
    if n * 2 == k:
        count += 1
        break

    # 2배를 했을때 k값을 넘어가게되는 경우
    # 2배를 해서 뺴주는 경우와, 2배안하고 더하는 경우중에 짧은 경우의 수를 구하여 반환한다.
    if n * 2 > k:
        minus_check = (n*2) - k
        plus_check = k - n
        count += min(plus_check, minus_check)
        break

    # 위의 경우가 모두 아닌 경우는 2배씩 처리
    count += 1
    n *= 2

print(count)