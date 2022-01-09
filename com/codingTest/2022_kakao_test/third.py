# fees	records	result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	[0, 591]
# [1, 461, 1, 10]	["00:00 1234 IN"]	[14841]
import math

def hourToMin(data:str):
    hour, min = data.split(':')
    return (int(hour) * 60) + int(min)

from collections import deque
def solution(fees, records):
    answer = []

    dic = {}

    for data in records:
        time, num, in_out = list(map(str, data.split()))
        if num not in dic:
            dic[num] = [(time, in_out)]
        else:
            dic[num].append((time, in_out))

    # print(dic)
    key_list = list(dic.keys())
    key_list.sort()
    # print(key_list)

    for i in key_list:
        temp_list = deque(dic[i])
        # 나가지않은경우 마지막 in data 를 담아준다.
        no_out_data = []
        # 총 보낸 시간
        all_count = 0

        # 마지막 데이터를 미리 빼둔다
        if len(temp_list) % 2 == 1:
            no_out_data.append(temp_list.pop())

        while temp_list:
            start = temp_list.popleft()
            end = temp_list.popleft()
            all_count += hourToMin(end[0]) - hourToMin(start[0])

        # 마지막 데이터까지 계산
        if no_out_data:
            all_count += hourToMin("23:59") - hourToMin(no_out_data[0][0])

        if all_count > fees[0]:
            answer.append(fees[1] + (math.ceil((all_count - fees[0]) / fees[2]) * fees[3]))
        else:
            answer.append(fees[1])


    return answer


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10],	["00:00 1234 IN"]))


