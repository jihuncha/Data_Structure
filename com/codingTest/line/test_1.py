# 대형 마트와 같은 상품 판매 회사는 물품을 외부 거래처로부터 구매하여 일정 마진을 더한 후 고객에게 판매합니다.
#
# 이때, 고객에게 상품을 판매하고 얻은 금액을 매출액이라 하고, 상품을 거래처로부터 구입할 때 지불한 금액을 매출원가라고 합니다.
#
# 매출원가를 구하는 방법에는 선입선출법, 후입선출법 2가지 방법이 있습니다.
#
# 선입선출법에서는 먼저 구매한 제품이 먼저 판매된다고 가정을 하는 반면,
#
# 후입선출법에서는 나중에 구매한 제품이 먼저 판매가 된다고 가정합니다.
#
# 상품 구입과 판매 기록이 주어졌을 때, 두 방법으로 각각 매출원가를 계산하여 비교하려고 합니다.
#
# 아래 표는 어느 마트의 상품 구입과 판매 기록을 나타냅니다. 상품의 종류는 1가지만 주어집니다.

# 활동	가격	수량
# 구입	300	6
# 구입	500	3
# 판매	1000	4
# 구입	600	2
# 판매	1200	1

# 위 표에 따르면 구입한 상품의 수는 총 11개, 판매한 상품의 수는 총 5개입니다.
# 선입선출법은 먼저 구매한 상품이 먼저 판매된다고 가정하기 때문에,
# 총판매수량 5는 모두 첫 번째 구입에서 가져온 상품을 판매한 것으로 가정합니다. 그렇기 때문에 매출원가는 1500원(= 300 x 5)입니다.
#
# 후입선출법은 나중에 구매한 상품이 먼저 판매된다고 가정하기 때문에,
# 첫 번째 판매에서 발생한 매출원가는 1800원(= 500 x 3 + 300 x 1)이고,
# 두 번째 판매에서 발생한 매출원가는 600원(= 600 x 1)입니다. 따라서 총매출원가는 2400원(= 1800 + 600)입니다.
#
# 참고로, 매출원가를 계산할 때 물품을 판매한 가격은 고려할 필요가 없습니다.
#
# 상품의 구입 또는 판매 활동과 그때 거래된 상품의 가격과 수량을 나타내는 문자열이 시간 순서대로 담긴 배열 record가 주어집니다.
# 선입선출법과 후입선출법을 따라 계산한 매출원가를 각각 a, b라고 할 때, [a, b] 형식으로 배열에 담아 return 하도록 solution 함수를 완성해주세요.
#
# 처음 갖고 있는 상품의 수와 매출원가는 0입니다.
# record의 길이는 1 이상 10,000 이하입니다.
# record의 원소는 "활동 가격 수량" 형식의 문자열입니다.
# 활동은 알파벳 대문자 'P' 또는 'S'입니다.
# 'P'는 구매를, 'S'는 판매를 나타냅니다.
# 가격은 1 이상 1,000 이하인 자연수입니다.
# 수량은 1 이상 1,000 이하인 자연수입니다.
# 갖고 있는 상품의 수량보다 많은 양의 판매하는 경우는 주어지지 않습니다.

# record	result
# ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]	[1500, 2400]
# ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]	[1800, 2700]
# ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]	[7100, 10700]

record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 2", "S 1200 1"]
record = ["P 300 6", "P 500 3", "S 1000 4", "P 600 1", "S 1200 2"]
record = ["P 100 4", "P 300 9", "S 1000 7", "P 1000 8", "S 700 7", "S 700 3"]

# stack queue 문제

from collections import deque

def solution(record):
    # stack, queue 선언
    stack = []
    queue = deque()

    # stack 과 queue 의 매출
    sell_stack = 0
    sell_queue = 0

    # 순회
    for i in range(len(record)):
        # 구입/판매여부, 가격, 수량
        a,b,c = record[i].split(' ')

        # 사는 경우
        if a == 'P':
            stack.append([b,c])
            queue.append([b,c])
        # 파는 경우
        if a == 'S':
            count_queue = int(c)
            count_stack = int(c)

            # queue 순회
            while queue:
                temp_queue = list(map(int,queue.popleft()))
                # 잔여횟수보다 적은 경우 - 남은것을 다시 queue에 담아준다.
                if count_queue - temp_queue[1] < 0:
                    temp_queue[1] = temp_queue[1] - count_queue
                    sell_queue += temp_queue[0] * count_queue
                    queue.appendleft(temp_queue)
                    break

                # 딱맞아 떨어지는 경우
                if count_queue - temp_queue[1] == 0:
                    temp_queue[1] = temp_queue[1] - count_queue
                    sell_queue += temp_queue[0] * count_queue
                    break

                # 부족한 경우 - queue를 다시 순회
                if count_queue - temp_queue[1] > 0:
                    sell_queue += temp_queue[0] * temp_queue[1]
                    count_queue = count_queue - temp_queue[1]

            # stack 도 동일한 방식
            while stack:
                temp_stack = list(map(int,stack.pop()))
                if count_stack - temp_stack[1] < 0:
                    temp_stack[1] = temp_stack[1] - count_stack
                    sell_stack += temp_stack[0] * count_stack
                    stack.append(temp_stack)
                    break

                if count_stack - temp_stack[1] == 0:
                    temp_stack[1] = temp_stack[1] - count_stack
                    sell_stack += temp_stack[0] * count_stack
                    break

                if count_stack - temp_stack[1] > 0:
                    sell_stack += temp_stack[0] * temp_stack[1]
                    count_stack = count_stack - temp_stack[1]

    return [sell_queue, sell_stack]

print(solution(record))