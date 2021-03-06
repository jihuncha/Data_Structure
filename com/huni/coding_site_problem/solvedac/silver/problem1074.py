# https://www.acmicpc.net/problem/1074

# 한수는 크기가 2N × 2N인 2차원 배열을 Z모양으로 탐색하려고 한다. 예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
#
# N > 1인 경우, 배열을 크기가 2N-1 × 2N-1로 4등분 한 후에 재귀적으로 순서대로 방문한다.
#
# 다음 예는 22 × 22 크기의 배열을 방문한 순서이다.
#
# N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
#
# 다음은 N=3일 때의 예이다.
#
# 입력
# 첫째 줄에 정수 N, r, c가 주어진다.
#
# 출력
# r행 c열을 몇 번째로 방문했는지 출력한다.
#
# 제한
# 1 ≤ N ≤ 15
# 0 ≤ r, c < 2N

# input 1
# 2 3 1

# output 1
# 11

# input 2
# 3 7 7

# output 2
# 63

# input 3
# 1 0 0

# output 3
# 0

# input 4
# 4 7 7

# output 4
# 63

# input 5
# 10 511 511

# output 5
# 262143

# input 6
# 10 512 512

# output 6
# 786432

################
# 아이디어가 떠오르지않는다..

import sys

input = sys.stdin.readline

n,r,c = map(int, input().split())

print(n,r,c)

# print(2 ** n)


####
# 1. 분할 정복 - 이걸어케알아내지..?신기하네


answer = 0

while n!= 0:

    n -= 1

    # 1사분면
    if r < 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 0

    # 2사분면
    elif r < 2 ** n and c >= 2 ** n:
        answer += (2 ** n) * (2 ** n) * 1
        c -= (2 ** n)

    # 3사분면
    elif r >= 2 ** n and c < 2 ** n:
        answer += (2 ** n) * (2 ** n) * 2
        r -= (2 ** n)

    # 4사분면
    else:
        answer += (2 ** n) * (2 ** n) * 3
        r -= (2 ** n)
        c -= (2 ** n)

    print(n,r,c)

print(answer)