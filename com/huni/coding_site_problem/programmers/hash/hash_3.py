# https://programmers.co.kr/learn/courses/30/lessons/42579

# 베스트앨범

# 문제 설명
# 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
#
# 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

# 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.
#
# 제한사항
# genres[i]는 고유번호가 i인 노래의 장르입니다.
# plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
# genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
# 장르 종류는 100개 미만입니다.
# 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
# 모든 장르는 재생된 횟수가 다릅니다.

# 입출력 예
# genres	plays	return
# ["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]

# 입출력 예 설명
# classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.
# 고유 번호 3: 800회 재생
# 고유 번호 0: 500회 재생
# 고유 번호 2: 150회 재생

# pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.
# 고유 번호 4: 2,500회 재생
# 고유 번호 1: 600회 재생
# 따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.


# index 는 고유 번호이다.
# 장르의 고유번호는 필요없어보임

def solution(genres, plays):
    answer = []

    # dic 생성
    dic = {}
    for idx, check in enumerate(genres):
        if check not in dic:
            # 재생횟수와 idx 보관
            dic[check] = [[plays[idx], idx]]
        else:
            dic[check].append([plays[idx],idx])

    # key 를 sum이 많은 순서대로 정렬
    dic_key = list(dic.keys())
    dic_key_list = []
    for i in dic_key:
        dic_key_list.append([i, sum(x[0] for x in dic[i])])
    dic_key_list.sort(key=lambda x:x[1], reverse=True)

    # 재생횟수 많은순서 / 그다음은 index 낮은 순서로 정렬
    for idx,mak_result in enumerate(dic_key_list):
        dic[mak_result[0]].sort(reverse=True, key=lambda x:(x[0],-x[1]))
        # 앞에 두개만 추출
        for j in dic[mak_result[0]][:2]:
            answer.append(j[1])

    # print(result_list)
    # print(dic.items())
    # result_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    # print(result_dic)

    # for i in dic.keys():
    #     print(sum(x[0] for x in dic[i]))

    # temp_list = list(dic.keys())
    # result_list = []
    # for i in temp_list:
    #     result_list.append([i, sum(dic[i][0])])
    # result_list.sort(key=lambda x:x[1], reverse=True)
    # print(result_list)

    # print(sum(dic[temp_list[0]]))
    # result_list = sorted(key=lambda x : sum(x[0] for x in dic[i]) for i in range(temp_list))
    # print(result_list)


    # key_sort = list(dic.keys())

    # key_sort.sort(key=lambda x : sum(x[0] for x in dic[key_sort[i]]) for i in range(len(key_sort)))

    # print(key_sort)
    # print((sum(x[0] for x in dic[key_sort[0]])))
    # print(key_sort)
    # temp_sort = sorted(key_sort, key=lambda x: sum(x[0] for x in dic[key_sort[0]]), reverse=True)
    # print(temp_sort)
    # print(key_sort)
    # print(key_sort.sort(sum(x[0] for x in dic[key_sort[0]])))


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


# 다른 사람 풀이

# 1.
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer

#2.
def solution(genres, plays):
    answer = []
    dic = {}
    album_list = []
    for i in range(len(genres)):
        dic[genres[i]] = dic.get(genres[i], 0) + plays[i]
        album_list.append(album(genres[i], plays[i], i))

    dic = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
    album_list = sorted(album_list, reverse=True)

    while len(dic) > 0:
        play_genre = dic.pop(0)
        print(play_genre)
        cnt = 0;
        for ab in album_list:
            if play_genre[0] == ab.genre:
                answer.append(ab.track)
                cnt += 1
            if cnt == 2:
                break

    return answer

class album:
    def __init__(self, genre, play, track):
        self.genre = genre
        self.play = play
        self.track = track

    def __lt__(self, other):
        return self.play < other.play
    def __le__(self, other):
        return self.play <= other.play
    def __gt__(self, other):
        return self.play > other.play
    def __ge__(self, other):
        return self.play >= other.play
    def __eq__(self, other):
        return self.play == other.play
    def __ne__(self, other):
        return self.play != other.play
