n = 1260
count = 0

coin_type = [500, 100, 50, 10]

# My Answer
# i = 0
# while i != len(coin_type):
#     a,b = divmod(n,coin_type[i])
#     count += a
#     n = b
#     i += 1
#
# print(count)

# Book answer

for i in coin_type:
    count += n // i
    n = n % i
print(count)
