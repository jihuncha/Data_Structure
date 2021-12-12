# 가장 비싸게 파는 경우

# input = [5,3,5,7,8]
# k = 3 -> 3개월동안 점진적으로 올라가는 경우의수

# 357, 578 2가지
# return 2

def countHighlyProfitableMonths(stockPrices, k):
    # k가 1인 경우에는 모든 경우가 다 해당됨
    if k == 1:
        return len(stockPrices)

    # 결과값을 저장할 result_count
    result_count = 0
    # 시작값
    start_value = stockPrices[0]

    # 임시로 저장할 count
    count = 1
    for i in range(1, len(stockPrices)):
        if start_value < stockPrices[i]:
            count += 1
        else:
            # count값 초기화
            count = 1
        # 시작값을 변경
        start_value = stockPrices[i]
        # 매번 돌때마다 count값이 k보다 큰경우 result를 올려준다.
        if count >= k:
            result_count += 1

    return result_count




print(countHighlyProfitableMonths([5,3,5,7,8], 3))