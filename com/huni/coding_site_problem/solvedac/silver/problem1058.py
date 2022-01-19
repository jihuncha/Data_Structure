# https://www.acmicpc.net/problem/1058

# 문제
# 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다.
# 어떤 사람 A가 또다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고, B와 친구인 C가 존재해야 된다.
# 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다. 가장 유명한 사람의 2-친구의 수를 출력하는 프로그램을 작성하시오.
#
# A와 B가 친구면, B와 A도 친구이고, A와 A는 친구가 아니다.
#
# 입력
# 첫째 줄에 사람의 수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 각 사람이 친구이면 Y, 아니면 N이 주어진다.
#
# 출력
# 첫째 줄에 가장 유명한 사람의 2-친구의 수를 출력한다.

# 3
# NYY
# YNY
# YYN

# 2

# 3
# NNN
# NNN
# NNN

# 0

# 5
# NYNNN
# YNYNN
# NYNYN
# NNYNY
# NNNYN

# 4

# 10
# NNNNYNNNNN
# NNNNYNYYNN
# NNNYYYNNNN
# NNYNNNNNNN
# YYYNNNNNNY
# NNYNNNNNYN
# NYNNNNNYNN
# NYNNNNYNNN
# NNNNNYNNNN
# NNNNYNNNNN

# 8

# 15
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNYNNNNNNN
# NNNNNNNYNNNNNNY
# NNNNNNNNNNNNNNY
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNYYNNNNNNNNNNN
# NNNNNYNNNNNYNNN
# NNNNNNNNNNNNNNY
# NNNNNNNNNNNNNNN
# NNNNNNNNYNNNNNN
# NNNNNNNNNNNNNNN
# NNNNNNNNNNNNNNN
# YNNYYNNNNYNNNNN

# 6

# 이게 누적합인가?
# 이거 다시보니까 dfs같은데..????아닌가..
import sys

input = sys.stdin.readline

count = int(input())

print(count)

data = []

for _ in range(count):
    temp_data = [0 if x == 'N' else 1 for x in list(map(str, input().split()))[0]]

    data.append(temp_data)

print(data)

# def dfs(start:int, end:int, count:int):
#
#
# for x in range(count):
#     for y in range(count):



