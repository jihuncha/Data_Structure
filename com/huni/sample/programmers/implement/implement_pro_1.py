# 문자열 압축

# https://programmers.co.kr/learn/courses/30/lessons/60057

# 데이터 처리 전문가가 되고 싶은 "어피치"는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 
# 
# 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 
# 
# 표현하는 알고리즘을 공부하고 있습니다.
# 
# 간단한 예로 "aabbaccc"의 경우 
# 
# "2a2ba3c"(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 
# 
# 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 
# 
# 예를 들면, "abcabcdede"와 같은 문자열은 전혀 압축되지 않습니다. "어피치"는 이러한 단점을 해결하기 위해 문자열을 
# 
# 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.
# 
# 예를 들어, "ababcdcdababcdcd"의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 
# 
# "2ab2cd2ab2cd"로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 "2ababcdcd"로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 
# 다른 예로, "abcabcdede"와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 3개 단위로 자른다면 
# 
# "2abcdede"가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.
# 
# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.
# 
# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.
# s는 알파벳 소문자로만 이루어져 있습니다.
# 
# 입출력 예
# s	result
# "aabbaccc"	7
# "ababcdcdababcdcd"	9
# "abcabcdede"	8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	17
# 입출력 예에 대한 설명
# 
# 입출력 예 #1
# 
# 문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.
# 
# 입출력 예 #2
# 
# 문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.
# 
# 입출력 예 #3
# 
# 문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.
# 
# 입출력 예 #4
# 
# 문자열을 2개 단위로 자르면 "abcabcabcabc6de" 가 됩니다.
# 문자열을 3개 단위로 자르면 "4abcdededededede" 가 됩니다.
# 문자열을 4개 단위로 자르면 "abcabcabcabc3dede" 가 됩니다.
# 문자열을 6개 단위로 자를 경우 "2abcabc2dedede"가 되며, 이때의 길이가 14로 가장 짧습니다.
# 
# 입출력 예 #5
# 
# 문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
# 따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
# 이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

# 문제 그대로 쫓아가면 해결되는데.. 구현이 어렵..
# 그리고 한글자인 case 못찾아서 질문 게시판에서 확인 후 해결 ('a')


#########################################
# 자르는 index 대로 자르면서 이전 글자와 비교함
# 이전 글자와 다른 경우는 결과 str에 담아준다.
# 같은 경우는 count 증가 시키면서 count가 2이상인 경우는 글자에 포함하여 넣어준다.
# 해당 전체 list에서 min 함수 사용하여 가장 적은 숫자 도출
# 시간이 너무 오래걸린다...
#########################################

def solution(s):
    answer = len(s)

    def make_str(index_size):
        # 초기 문자열
        before_str = s[0:index_size]
        # 초기 count
        count = 1
        # 결과 문자열
        result_str = ""

        # 다음 문자열 부터 index_size 만큼 짜르면서 체크를 한다.
        for i in range(index_size, len(s) + 1, index_size):
            # 다음 문자열
            temp_str = s[i:i + index_size]
            # 다음 문자열이 이전 문자열과 같은 경우 count 증가 시킨다.
            if before_str[:] == temp_str[:]:
                count += 1
            # 이전 문자열이 다른 경우는 count와 함께 결과 str에 더해준다.
            else:
                result_str += str(count) + before_str if count >= 2 else before_str
                before_str = temp_str[:]
                count = 1
        # 잔여 문자열 처리 (8자리이면서 3으로 짜른 경우...) -> else에 안탄경우
        result_str += str(count) + before_str if count >= 2 else before_str

        return result_str

    # 결과에 다 더해준다.
    all_result_list = []
    for i in range(1, len(s) // 2 + 1):
        all_result_list.append(len(make_str(i)))

    # print(all_result_list)

    # 'a'인 경우
    return min(all_result_list) if all_result_list else answer

print(solution("a"))
