# lst = ['+7', '+6', '+5', '+4']
# a = dict.fromkeys(lst, 'код страны')
# # print(a)
#
# b = a.copy()
# print(b)
#
# b['+7'] = 'value'
# print(b)
# print(a)
# print(id(a))
# print(id(b))

# print(b.get('+7'))
# print(b.setdefault('+7'))
# print(b.setdefault('+9'))
# print(b.setdefault('+8', 'восемь'))
# print(b)
# print(b.pop('+9'))
# print(b)
# print(b.pop('abc', False))
# print(b)
# print(b.popitem())
# print(b.keys())
#
# for x in b:
#     print(x)

# print(b.values())
#
# for x in b.items():
#     print(x)

# for key, value in b.items():
#     print(key, value)

#-----------------
d = dict(one = 1, two = 2, three = 3, four = 4)
d_1 = {2: "неуд", 3: "уд", 4: "хор", 5: "отл"}

# print(d)
# print(d_1)
#
# d.update(d_1)
# print(d)

# d_3 = {**d, **d_1}
# print(d_3)
#
# d_4 = {**d_1, **d}
# print(d_4)
d_5 = d | d_1
print(d_5)