# https://www.acmicpc.net/problem/1024

# 수열의 합

# 문제
# N과 L이 주어질 때, 합이 N이면서, 길이가 적어도 L인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 L이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이고, L은 2보다 크거나 같고, 100보다 작거나 같은 자연수이다.
#
# 출력
# 만약 리스트의 길이가 100보다 작거나 같으면, 연속된 수를 첫째 줄에 공백으로 구분하여 출력한다. 만약 길이가 100보다 크거나 그러한 수열이 없을 때는 -1을 출력한다.

# 입력
# 18 2

# 출력
# 5 6 7

# 입력
# 18 4

# 출력
# 3 4 5 6

# 입력
# 18 5

# 출력
# -1

# 입력
# 45 10

# 출력
# 0 1 2 3 4 5 6 7 8 9

# 입력
# 1000000000 2

# 출력
# 199999998 199999999 200000000 200000001 200000002
import sys

input = sys.stdin.readline

n,l = map(int, input().split())

# print(n,l)




### 수학이 참 어렵군
# https://sexycoder.tistory.com/97

temp = -1
for i in range(l, 101):
    temp_sum = (i * (i-1)) // 2

    if n - temp_sum < 0:
        break

    if temp_sum > 0 and (n-temp_sum) % i == 0:
        temp = (n-temp_sum) // i
        for j in range(temp, temp + i):
            print(j, end=' ')
        break

if temp == -1:
    print(temp)


