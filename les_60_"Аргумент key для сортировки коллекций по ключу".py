# def id_odd(x):
#     return x % 2
#
#
# a = [4, 3, -10, 1, 7, 12]
# b = sorted(a, key=id_odd)
# print(b)

#-----------------------------
a = [4, 3, -10, 1, 7, 12]                   # верхняя запись по другому

# b = sorted(a, key=lambda x: x % 2)
# print(b)

a.sort(key=lambda x: x % 2)                 # еще 1 запись равнозначна вышеизложенным
print(a)