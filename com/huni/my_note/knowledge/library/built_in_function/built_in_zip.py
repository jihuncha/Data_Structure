number = [1,2,3,4]
name = ['my', 'name', 'is', 'jihun']

dic = {}
for a,b in zip(number,name):
    print(a,b)
    dic[a] = b

print(dic)

temp = [1,2,3,4,5,6,7,8,9]

for a,b in zip(temp, temp[1:]):
    print(a,b)

# com/huni/coding_site_problem/programmers/hash/hash_1.py 참고
temp = ["abc", "eqes", "ewqeqweqwe", "dssddwssddd","abcede"]

temp.sort()
for a,b in zip(temp, temp[1:]):
    # print(a,b)
    if b.startswith(a):
        print("a : ", a, " b : ", b)