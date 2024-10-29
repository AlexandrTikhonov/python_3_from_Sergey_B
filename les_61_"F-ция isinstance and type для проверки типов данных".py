# a = 5
#
# print(isinstance(a, int))
# print(isinstance(a, float))

# #---------------
# b = True
# print(isinstance(b, bool))
# print(isinstance(b, int))
#
# print(type(b) == bool)
# print(type(b) == int)

#--------------------
# data = (4.5, 8.7, True, 'книга', 8, 10, -11, [True, False])

# s = 0
# for x in data:
#     if isinstance(x, float):
#         s += x
#



# s = sum(filter(lambda x: isinstance(x, float), data))          # запишем решение чуть по другому (ниже)

# s = sum(filter(lambda x: type(x) is int, data))               # так как булевое значение наследовано от int, то решение нужно доработать и успользовать f-цию type
#
# print(s)

#---------------
#                                      ПРОВЕДЕМ ПРОВЕРКУ ОТНОШЕНИЯ ЭЛЕМЕНТА СРАЗУ К НЕСКОЛЬКИМ ТИПАМ
a = 5.5

print(isinstance(a, (int, float)))      # равносильно записи         print(instance(a, int) or instance(a, float))