str_test = 'abcdefg'

# print(str_test[:2])

for i in range(0,len(str_test),2):
    print(i)
    print(str_test[i:i+2])

print(str_test.index('b'))