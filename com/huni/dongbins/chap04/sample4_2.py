# 시각

# N 이 입력되면 00시 00분 00초 부터 N시 59분 59초 까지 3이 포함되는 경우의 수를 구하는 프로그램

# input
# 5

# output
# 11475

n = int(input())

count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

# book_answer
# H를 입력받기
# h = int(input())
#
# count = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1
#
# print(count)