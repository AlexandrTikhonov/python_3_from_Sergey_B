# b = map(int, ['1', '2', '3', '5', '7'])
# # b = (int(x) for x in ['1', '2', '3', '5', '7'])                  # тоже самое, что и выше
#
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))
# # print(next(b))               # --> StopIteration
#
#
# # for x in b:                  # тоже самое, что и выше
# #     print(x, end=" ")
#
# # a = list(b)
# # print(a)
#
# # a = sum(b)
# # print(a)
#
# a = max(b)
# print(a)

# #-------------------
# cities = ["Москва", "Астрахань", "Самара", "Уфа", "Смоленск", "Тверь"]
#
# # b = map(len, cities)         # получим список длин названия городов из списка
# #
# # a = list(b)
# # print(a)
#
# #------------------
# b = map(str.upper, cities)
#
# a = list(b)
# print(a)

#--------------------
s = map(int, input().split())
a = list(s)
print(a)