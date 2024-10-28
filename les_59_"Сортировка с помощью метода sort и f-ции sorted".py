# # работа происходит в консоле pycharm
a = [4, 3, -10, 1, 7, 12.5]
#
# a.sort()
# a
#
# a.sort(reverse=True)          # вывод задом наперед
# a

# #-------------------
# b = sorted(a)
# print(a)
# print(b)
#
# b1 = sorted(a, reverse=True)
# print(b1)

# #-------------------
# r = ("Волга", "Лена", "Дон", "Енисей")       # f-ция sorted() для кортежа, т.е. для неизменяемого типа данных
# r1 = sorted(r)
# print(r1)

# #-------------------
# p = sorted("python")
# print(p)

#---------------------
d = {'river': 'река', 'house': 'дон', 'tree': 'дерево', 'road': 'дорога'}
d1 = sorted(d)                                                                  # f-ция sorted() для ключей словаря
print(d1)

d2 = sorted(d.values())                                                         # f-ция sorted() для значений словаря
print(d2)

d3 = sorted(d.items())                                                          # f-ция sorted() для ключей и значений словаря
print(d3)

print(dict(sorted(d.items())))