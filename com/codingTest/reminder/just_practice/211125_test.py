root = [1,2,3,4,5]

def test(input:list):
    print(id(input))

    temp = [input]
    print(id(temp[0]))

    for i in temp:
        for j in range(len(i)):
            print(j)
            input[j] += 1

    return input

print(test(root))