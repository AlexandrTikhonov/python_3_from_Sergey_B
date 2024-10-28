# a = (x ** 2 for x in range(6))
#
# #print(a)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# #--------------------------
# gen = (x ** 2 for x in range(6))
# for x in gen:
#     print(x)
#
# for x in gen:
#     print(x)

#----------------------------
a = (x ** 2 for x in range(6))
print(list(a))

a = (x ** 2 for x in range(6))
print(set(a))

a = sum(x ** 2 for x in range(6))
print(a)

a = (x ** 2 for x in range(6))
print(sum(a))

a = (x ** 2 for x in range(6))
print(max(a))

a = (x ** 2 for x in range(6))
print(min(a))