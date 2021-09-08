# 편집 거리

# 문자열 A,B -> A를 편집하여 B를 만들기
#
# 1. 삽입
# 2. 삭제
# 3. 교체

# sunday -> saturday 최소편집거리 3

# cat
# cut

# 1

# sunday
# saturday

# 3

# 문자열은 1~5000

data = list(map(str, input()))

output = list(map(str, input()))

print(data, output)

## 감도안오네 ㅋ

# 최소 편집거리를 담을 2차원 테이블 초기화 -> 최소 편집 거리를 계산해 테이블에 저장

# 1. 두문자가 같은 경우 -> dp[i][j] = dp[i-1][j-1]
# 2. 다른 경우
# dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
#
# 1. 행과 열에 해당하는 문자가 서로 같은경우는 왼쪽위의 숫자 그대로
# 2. 행과 열이 해당하는 문자가 다른경우 왼쪽(삽입) / 위쪽(삭제) / 왼쪽위(교체) 중 작은수를 골라 1을 더한다.

n = len(data)
m = len(output)

dp = [[0] * (m+1) for _ in range(n+1)]

# print(dp)

for i in range(1, n+1):
    dp[i][0] = i

for j in range(1, m+1):
    dp[0][j] = j

for i in range(1, n+1):
    for j in range(1, m+1):
        if data[i-1] == output[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n][m])