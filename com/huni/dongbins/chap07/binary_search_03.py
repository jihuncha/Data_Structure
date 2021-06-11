# 떡볶이 떡 만들기

# 높이 H를 지정하면 줄지어진 떡을 한 번에 절단
#
# 높이가 H보다 긴 떡은 H위 부분이 짤리고, 낮은 떡은 짤리지 않는다.
#
# 19 14 10 17 -> 15만큼 짜른다 -> 15 14 10 15 -> 잘린 떡은 4 0 0 2 --> 손님은 6만큼 가져감
#
# 손님이 왓을때 요청한 총 길이가 M일때 적어도 M만큼의 떡을얻기 위해서 절단기에 설정할 수 있는 최대 높이를 구하시오
#
# * 첫번 째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어짐 (1 <= N <= 1,000,000, 1<= M <= 2,000,000,000)
# * 둘째 줄에는 떡의 개별 높이가 주어짐 // 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈수있다, 높이는 10억보다 작거나 같은 양의 정수 또는 0이다
#
# 입력 예시
# 4 6
# 19 15 10 17
#
# 출력예시
# 15

###################################################
### 절단기 높이가 10억인걸 보고 이진 탐색임을 알아야한다!!!


n, m = input().split()

data = list(map(int, input().split()))

start = 0
end = max(data)

temp_result = 0
while start <= end:
    mid = (start + end) // 2

    cutting = sum(list(map(lambda x:x - mid if x - mid > 0 else 0, data)))

    if cutting >= int(m):
        temp_result = mid
        start = mid + 1

    if cutting < int(m):
        end = mid - 1

print(temp_result)