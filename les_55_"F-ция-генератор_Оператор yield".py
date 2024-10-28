# def get_list():
#     for x in [1, 2, 3, 4]:
#         yield x
#
#
# a = get_list()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))   # --> StopIteration

# -------------
def get_list():
    for i in range(1, 10):
        a = range(i, 11)
        yield sum(a) / len(a)


a = get_list()
print(list(a))
