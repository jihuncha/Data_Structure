dic ={1: 0.125, 2: 0.42857142857142855, 3: 0.5, 4: 0.5, 5: 0.0}

# print(dic.get())
test = sorted(dic, key=dic.get, reverse=True)

print(test)

