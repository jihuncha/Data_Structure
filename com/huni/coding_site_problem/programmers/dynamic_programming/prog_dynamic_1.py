# https://programmers.co.kr/learn/courses/30/lessons/42895

# N으로 표현

# 문제 설명
# 아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

# 12 = 5 + 5 + (5 / 5) + (5 / 5)
# 12 = 55 / 5 + 5 / 5
# 12 = (55 + 5) / 5
#
# 5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
# 이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

# 제한사항
# N은 1 이상 9 이하입니다.
# number는 1 이상 32,000 이하입니다.
# 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
# 최솟값이 8보다 크면 -1을 return 합니다.

# 입출력 예
# N	number	return
# 5	12	4
# 2	11	3
# 입출력 예 설명

# 예제 #1
# 문제에 나온 예와 같습니다.
#
# 예제 #2
# 11 = 22 / 2와 같이 2를 3번만 사용하여 표현할 수 있습니다.

################
# 생각하는게 어렵다
# 처음에 5
# 두번쨰에 55(5를 2번 이어 붙임)
# 10(5+5), 25(5*5), 1(5/5), 0(5-5)
# 세번쨰에 555(5를 3번 이어붙임)
# 15((5+5)+5), 5((5+5)-5), 2((5+5)/5), 50((5+5)*5)
# 30((55)+5), 20((55)-5)), 5((55)/5), 125((55)*5)
# ...
################

def solution(N, number):
    answer = 0

    dp = [[]]

    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    temp.append(k + l)
                    if k - l >= 0:
                        temp.append(k - l)
                    temp.append(k * l)
                    if l != 0 and k != 0:
                        temp.append(k // l)
        # 이어 붙이기
        temp.append(int(str(N) * i))

        if number in temp:
            return i
        dp.append(list(set(temp)))

    return answer


# test = ['(', '1', '+', '2', ')', '*', "10"]
#
# result = ''
# for i in test:
#     result += i
# print(eval(result))

## 풀이 1
# 주어진 숫자 N으로 각 횟수당 만들수 있는 숫자 조합을 만든다.
# 만들어진 숫자 조합에 number로 주어진 숫자가 있는지 확인한다.
# 만약 있다면 그 시점에서의 횟수를 답으로 리턴한다.
# 없다면 횟수를 하나 늘리고 가능한 숫자 조합을 만들고 1~3을 반복한다.

###############
# https://gurumee92.tistory.com/164
# 1. [ SET x 8 ] 인 리스트를 만듭니다. 각각 N을 1개로 표현하는 수들의 집합, 2개로 표현하는 수들의 집합, ... 8개로 표현하는 수들의 집합이 저장됩니다.
# 2. 8개의 SET에 개수만큼 N을 연달아 표현되는 수를 집어넣어줍니다.
# 3. 숫자 N에 대해서 n개를 사용해서 표현한 수의 일반화 수식을 코드로 표현합니다.
#
# 1. i에 대해서 1-8까지 순회합니다.
# 1. j에 대해서 0-i까지 순회합니다.
# 1. j개를 사용해서 만든 수들의 집합 s[j]를 다음과 같이 순회합니다.
# 1. i-j-1을 사용해서 만든 수들의 집합 s[i-j-1]를 다음과 같이 순회합니다.
# 1. op1(s[j] 순회 수)과 op2(s[i-j-1] 순회 수)를 사칙연산합니다. 나눗셈 시 op2는 0이 되면 안됩니다.
# 2. 사칙연산한 결과 값을 집합 s[i]에 추가합니다.
# 2. 만약 number가 s[i]에 존재한다면, 반복을 멈추고 i+1번을 반환합니다.
# 2. 8번을 순회했음에도, number를 못찾는다면, -1을 반환합니다.
###############

def solution(N, number):
    # 허뎝님의 수정 피드백 -> 테스트 케이스가 바뀌면서 예외 사항을 추가해야 함.
    if N == number:
        return 1

    # 1. [ SET x 8 ] 초기화
    s = [set() for x in range(8)]

    # 2. 각 set마다 기본 수 "N" * i 수 초기화
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    # 3. n 일반화
    #   {
    #       "n" * i U
    #       1번 set 사칙연산 n-1번 set U
    #       2번 set 사칙연산 n-2번 set U
    #       ...
    #       n-1번 set 사칙연산 1번 set,
    #    }
    # number를 가장 최소로 만드는 수 구함.
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        if number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer


## 풀이2
# 이게 제일 이해하기 쉽다!!!
# https://moondol-ai.tistory.com/272
def solution(N, number):
    # index n이 몇번 사용 되었는가 dp[1] = 1번, dp[3] = 3번
    dp = [[]]
    # 문제조건상 8보다 크면 -1 리턴
    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            # j번 사용한 경우의 원소 나열
            for k in dp[j]:
                # i-j번 사용한 경우의 원소 나열
                for l in dp[i - j]:
                    # 더하기
                    temp.append(k + l)
                    # 빼기
                    if k - l >= 0:
                        temp.append(k - l)
                    # 곱하기
                    temp.append(k * l)
                    # 나누기
                    if l != 0 and k != 0:
                        temp.append(k // l)
        # 이어 붙이기
        temp.append(int(str(N) * i))

        if number in temp:
            return i
        dp.append(list(set(temp)))

    return -1
