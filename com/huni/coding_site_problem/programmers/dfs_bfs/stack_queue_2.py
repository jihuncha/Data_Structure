# https://programmers.co.kr/learn/courses/30/lessons/42583

# 다리를 지나는 트럭

# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다.
# 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
# ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.
#
# 예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.
#
# 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
# 0	            []	            []	        [7,4,5,6]
# 1~2	        []	            [7]	        [4,5,6]
# 3	            [7]	            [4]	        [5,6]
# 4	            [7]	            [4,5]	    [6]
# 5	            [7,4]	        [5]	        [6]
# 6~7	        [7,4,5]	        [6]	        []
# 8	            [7,4,5,6]	    []	        []

# 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.
#
# solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
# 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.
#
# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

# bridge_length	weight	truck_weights	return
# 2 	        10	            [7,4,5,6]	8
# 100	        100	            [10]	101
# 100	        100	[10,10,10,10,10,10,10,10,10,10]	110

import collections

#############################
# 아무리 해도 안되서 풀이보기
# 1. 문제 절차대로 할려고 했으나 안됨
# 2. 생각은 queue를 가지고 holding 되어 있는 무게를 체크 하면서 시간지남에 따라 변경되는 사항을 전부 체크 할려했으나, 시간도 너무 오래 걸리고 해결이 안됨.
#############################

# 다른 사람 풀이
def solution(bridge_length, weight, truck_weights):
    answer = 0

    # 길이로 다리 자체를 작성
    q = [0] * bridge_length

    # 시간이 지남에 따라 이동하는 것을 표현
    while q:
        answer += 1
        # 맨 왼쪽 제거
        q.pop(0)

        # 잔여 리스트가 있는 경우
        if truck_weights:
            # q의 합과 다음 합이 무게 보다 작은 경우
            # 리스트를 제거하면서 더해준다.
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                # 아닌 경우는 그냥 0 을 더한다.
                q.append(0)

                
    # holding_queue = collections.deque()
    # truck_weights_second = collections.deque(truck_weights)
    # time_start = collections.deque()
    # holding_weight = 0
    #
    # while True:
    #     answer += 1
    #
    #     if truck_weights_second:
    #         temp_data = truck_weights_second.popleft()
    #
    #         if not holding_queue:
    #             holding_queue.append(temp_data)
    #             time_start.append(answer)
    #             holding_weight += temp_data
    #         else:
    #             if holding_weight + temp_data <= weight:
    #                 holding_queue.append(temp_data)
    #                 time_start.append(answer)
    #                 holding_weight += temp_data
    #             else:
    #

                    # time_temp = time_start.popleft()
                    # answer += bridge_length + time_temp - answer
                    # holding_weight -= holding_queue.popleft()
                    #
                    # holding_queue.insert(temp_data, 0)
                    # time_start.insert(answer, 0)

                    # if not holding_queue:
                    #     holding_queue.append(temp_data)
                    #     time_start.append(answer)
                    #     holding_weight = temp_data
                    # holding_queue.append()

        # else:
        #     if holding_queue:
        #         answer += bridge_length + time_start.popleft() - answer
        #         holding_queue.popleft()
        #     break

    return answer

print(solution(2, 10,  [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))

    # check_time = 0
    #
    # # 대기 상태에 있는 queue 선언
    # holding_queue = collections.deque()
    # # queue 형태로 변경
    # temp_truck_data = collections.deque(truck_weights)
    # start_time = collections.deque()
    # result_list = []
    #
    # while True:
    #     # 초기 첫번쨰 데이터 추출
    #     answer += 1
    #     if len(temp_truck_data):
    #         hold_data = temp_truck_data.popleft()
    #         holding_queue.append(hold_data)
    #         start_time.append(answer)
    #
    #     while True:
    #         print(temp_truck_data)
    #         print(answer)
    #         # 두번쨰 데이터 추출
    #         if len(temp_truck_data):
    #             temp_data = temp_truck_data.popleft()
    #             answer += 1
    #         else:
    #             answer += weight - start_time.popleft()
    #             print(answer)
    #             result_list.append(holding_queue.popleft())
    #
    #         if hold_data + temp_data <= weight:
    #             hold_data = temp_data + hold_data
    #             start_time.append(answer)
    #             holding_queue.append(temp_data)
    #
    #             if answer - start_time[0] >= bridge_length:
    #                 result_data = holding_queue.popleft()
    #                 hold_data = hold_data - result_data
    #                 start_time.popleft()
    #                 result_list.append(result_data)
    #         # 아닌 경우는 끝날때까지 돈다
    #         else:
    #             answer += weight - start_time.popleft()
    #             result_list.append(holding_queue.popleft())
    #
    #         if len(result_list) == len(truck_weights):
    #             break
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #

    # result_data = list()
    #
    # # 트럭에서 다 꺼내서 처리할때까지 반복한다.
    # while True:
    #     # 첫번쨰를 holding 에 이동
    #     answer += 1
    #     count += 1
    #     hold_data = temp_truck_data.popleft()
    #     holding_queue.append([answer, hold_data])
    #
    #     while count >= bridge_length:
    #         if holding_queue:
    #             result_data.append(holding_queue.popleft())
    #             count = answer - count
    #         else:
    #             break
    #
    #     # 끝
    #     if len(result_data) == len(truck_weights):
    #         break
    #
    #     # 다음 데이터 추출
    #     next_data = temp_truck_data.popleft()
    #     if hold_data + temp_truck_data

        # print(hold_data)
        # my_left_time = 0
        #
        # # 대기 상태에 넣고 더해준다.
        # holding_queue.append(hold_data)
        # print(holding_queue)
        # answer += 1
        # # my_left_time += 1
        # # temp_clock = 0
        #
        # while holding_queue:


        # for i in range(len(truck_weights)):
        #     answer += 1
        #     my_left_time += 1
        #
        #     if truck_weights[i] + hold_data <= weight:
        #         if len(holding_queue) <= 2:
        #             temp_clock = answer
        #         holding_queue.append(truck_weights[i])
        #
        #         if my_left_time >= bridge_length:
        #             my_left_time = answer - temp_clock
        #             holding_queue.popleft()
        #             if holding_queue:
        #                 hold_data = holding_queue[0]
        #     else:
        #         break
