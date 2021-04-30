def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


# g_temp = get_natural_number()
# for _ in range(0,100):
#     print(next(g_temp))

def generator_f():
    yield 1
    yield 'string'
    yield True

g = generator_f()
print(g)
print(next(g))
print(next(g))
print(next(g))