# https://programmers.co.kr/learn/courses/30/lessons/42586

# 기능개발

# 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.
#
# 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.
#
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를
# return 하도록 solution 함수를 완성하세요.
#
# 제한 사항
# 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
# 작업 진도는 100 미만의 자연수입니다.
# 작업 속도는 100 이하의 자연수입니다.
# 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

# progresses	speeds	return
# [93, 30, 55]	[1, 30, 5]	[2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]



#############################
# 내부 주석 참고
#############################

import collections

temp =[93, 30, 55]
temp_2 = [1, 30, 5]

def solution(progresses, speeds):
    answer = []

    # 시간을 줄이기 위해(popleft) Queue 사용
    day_check = collections.deque(progresses)
    temp_speed = collections.deque(speeds)

    # day_check queue 가 빌떄까지 반복
    while day_check:
        # 첫번째요소
        left_data = day_check.popleft()
        left_data_speed = temp_speed.popleft()

        # 첫번쨰 요소가 100이 될때까지 다른 요소들도 같이 올려준다
        while left_data < 100:
            for idx in range(len(day_check)):
                if day_check[idx] < 100:
                    day_check[idx] += temp_speed[idx]
                    # 100 이상이 된 경우는 그냥 100으로 처리
                    if day_check[idx] > 100:
                        day_check[idx] = 100
            left_data += left_data_speed

        # 100 이 되면 상기 while문을 벗어나서 남은 list 체크 한다.

        # count 하기 위한 숫자 - 맨 왼쪽 숫자가 100이 됬으니 1부터
        count = 1
        # list 복사
        stop_list = list(day_check)
        # 다음 list가 100 인 경우는 동시에 삭제하면서 카운트 증
        for i in stop_list:
            if i == 100:
                day_check.popleft()
                temp_speed.popleft()
                count+=1
            else:
                # 다음 list가 100이 아닌 경우는 빠져 나간다.
                break
        # 경과 리스트에 더해준다.
        answer.append(count)
    return answer

print(solution(temp, temp_2))


# 다른사람 풀이 1.
# zip이 뭐지??
# zip() 은 동일한 개수로 이루어진 자료형을 묶어 주는 역할
# 답을 봐도 하나도 이해가 안감...

def solution(progresses, speeds):
    Q=[]
    # print(zip(progresses, speeds))
    for p, s in zip(progresses, speeds):
        # print(p,s)
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

print(solution(temp, temp_2))


# 다른사람 풀이 2.
# 이 코드가 심플하고 깔끔
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer

print(solution(temp, temp_2))