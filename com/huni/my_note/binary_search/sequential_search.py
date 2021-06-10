# 순차 탐색

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1    # 현재 위치 반환 (인덱스는 0부터 시작하므로)

print("생성할 원소의 개수 와 한 칸 띄고 찾을 문자열을 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력해주세요")
array = input().split()

print(sequential_search(n,target,array))

# 입력
# 5 Dongbin
# Hanul Jonggu Dongbin Taeil Sangwook

# 출력
# 3