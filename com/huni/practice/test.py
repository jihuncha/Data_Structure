# list_temp = ["1","2","3","4","5"]
#
# print("/".join(list_temp[:]))
#
# # temp = [1, 20, 2222, 2323, 26231]
# test = ['3', '333335', '30', '34']
#
# for i in test:
#     if len(i) < 6:
#         print(i * 6)

# list_test = [89, 8989]
#
# result = sorted(list_test, key=lambda x: str(x) * 3, reverse=True)
#
# print(result)

# def solution(citations):
#     citations.sort()
#     h = 0
#
#     for _ in range(len(citations)):
#         # h번 이상 인용된 논문이 h편 이상
#         # 배열의 끝에서 h번째의 값이 h보다 작거나 같은지
#         if citations[-(h + 1)] <= h:
#             break
#         h += 1
#
#     return h
#
# print(solution([22, 42]))


temp = [1,2,3,4,5,6,7]

print(temp[::2])