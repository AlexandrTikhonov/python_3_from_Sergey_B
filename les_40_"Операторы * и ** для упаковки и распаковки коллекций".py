# x, y = (1, 2)
# print(x, y)

# #---------------
# x, *y = (1, 2, 3, 4)
# print(x, y)

# #-----------------
# *x, y = (1, 2, 3, 4)
# print(x, y)

# #------------------
# x, *y = [1, "a", True, 4]
# print(x, y)

# #--------------------
# *x, y, z = "Hello Python"
#
# print(x)
# print(y)
# print(z)

# #----------------------
# d = -5, 5
# print(range(*d))
# print(list(range(*d)))

#------------------------
d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:'five'}
d_1 = {6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
print(d)
print({*d})
print(*d.values())
print(*d.items())
d_2 = {**d, **d_1}
print(d_2)