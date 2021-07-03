# https://programmers.co.kr/learn/courses/30/lessons/42577

# 전화번호 목록

# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.

# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
#
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.
#
# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.
#
# 입출력 예제
# phone_book	return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true
# ["12","123","1235","567","88"]	false
# 입출력 예 설명
# 입출력 예 #1
# 앞에서 설명한 예와 같습니다.
#
# 입출력 예 #2
# 한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.
#
# 입출력 예 #3
# 첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

import bisect
import collections


def solution(phone_book):
    answer = True

    # temp_phone_book = sorted(phone_book, key=lambda x: len(x))
    #
    # dic = {}
    # for check in temp_phone_book:
    #     if check[:len(temp_phone_book[0])] not in dic:
    #         dic[check[:len(temp_phone_book[0])]] = 1
    #     else:
    #         answer = False
    #         break

    # answer = True
    #
    # temp_phone_book = sorted(phone_book, key=lambda x: len(x))
    #
    # dic = {}
    # for check in temp_phone_book:
    #     if check[:len(temp_phone_book[0])] not in dic:
    #         dic[check[:len(temp_phone_book[0])]] = 1
    #     else:
    #         answer = False
    #         break

    # deque_pb = collections.deque(phone_book)
    # while deque_pb:
    #     temp = deque_pb.popleft()
    #     for str_check in deque_pb:
    #         if temp in str_check:
    #             answer = False
    #             break

    phone_book.sort()
    for my_str in range(len(phone_book) - 1):
        if len(phone_book[my_str]) <= len(phone_book[my_str + 1]):
            if phone_book[my_str] == phone_book[my_str + 1][:len(phone_book[my_str])]:
                return False

    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

# 이거 true 나와야할듯?
print(solution(["12", "1322", "1324"]))
# print(solution(["11111", "11"]))
# print(solution(["1111", "11112"]))


#1 zip 학습 필요
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


# 정석 hash -> 이게 시간초과가 안나는구나?
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
