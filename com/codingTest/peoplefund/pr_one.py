

# 가장 큰수 만들기

# 7596801

# 1806579
import collections


def getLargestNumber(num:str):

    # string으로 받은 num 을 인자 int인 list로 변경
    num = list(map(int, num))

    # 이중 for문으로 크기 판별하여 서로 홀수/짝수가 맞는 경우에 swap 진행
    # for i in range(1, len(num)):
    #     for j in range(i-1, i):
    #         print(i,j)
    #         if num[i] > num[j] and (num[i] % 2 == num[j] % 2):
    #             num[i],num[j] = num[j], num[i]

    # 결과를 담을 string
    result = ""
    # 맨 처음값으로 진행
    temp_list = [num[0]]
    for i in num[1:]:
        # 만약 list가 비어잇는 경우 예외처리
        if not temp_list:
            temp_list.append(i)
        else:
            temp = temp_list[0]
            # 인접한 같은 짝수/홀수인 경우
            if temp % 2 == i % 2:
                temp_list.append(i)
            # 인접한것이 짝수/홀수가 다른 경우는 기존의 list를 정렬하여 string에 추가해준다.
            else:
                temp_list.sort(reverse=True)
                result += ''.join(str(x) for x in temp_list)
                temp_list = [i]
    # 남아있는 list가 있는 경우 반환
    if temp_list:
        temp_list.sort(reverse=True)
        result += ''.join(str(x) for x in temp_list)


    # string 으로 반환
    return result


print(getLargestNumber("1806579"))