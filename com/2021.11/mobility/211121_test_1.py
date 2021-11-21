# 전화번호 서치

A = ["pim", "pom"]
B = ["99999999", "777888999"]
P = "88999"

# pom
#


A = ['sander', 'amy', 'ann', 'michael']
B =['123456789', '234567890', '789123456', '123123123']
P = '1'

#ann

#
A = ['adam', 'eva', 'leo']
B= ['121212121', '111111111', '444555666']
P = '112'

#NO CONTACt

def solution(A, B, P):

    # dictionary로 생성 (번호 / 이름)
    dic = dict(zip(B,A))
    # key 로 임시 리스트 생성
    temp_list = list(dic.keys())
    # 결과를 담을 list
    result_list = []

    # P가 포함된 내용 확인
    for i in temp_list:
        if P in i:
            result_list.append((dic[i],i))

    # 해당 list가 없는 경우
    if len(result_list) == 0:
        return "NO CONTACT"
    # 해당 list 1개 인 경우
    elif len(result_list) == 1:
        return dic[result_list[0][1]]
    # 여러개인 경우는 이름 순으로 정렬하여 가장 작은 값을 반환한다.
    else:
        result_list.sort()
        return dic[result_list[0][1]]

    pass

print(solution(A,B,P))
