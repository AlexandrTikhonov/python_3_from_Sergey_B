# a = {1, 2, 3, 4, "python"}
# b = set([1, 1, 2, 2, 3, 3])
#
#
# print(a)
# print(b)

#------------------
# sities = ["Ульяновск", "Москва", "Калуга", "Тюмень", "Ульяновск", "Москва", "Калуга", "Тюмень", "Ульяновск", "Москва"]
# s = set(sities)

# for i in s:
#     print(set(s))
#     break

# it = iter(s)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
#
# print(len(s))

#---------------
# print("Москва" in s)
#
# print("abc" in s)

# d = s.add("Казань")
#
# print(d)
# print(s)

b = set()
print(b)

b.add(7)                                     # добавить 1 элемент
print(b)

b.add(3)
print(b)

b.update(['a', 'b', (1, 2)])                 # добавить несколько элементов
print(b)

b.update('abrakadabra')
print(b)

b.discard((1, 2))                             # удалить элемент
print(b)

b.discard(8)                                  # удалить несуществующий элемент
print(b)

b.remove('b')                                   # удалить элемент
print(b)

print(b.pop())
print(b)

print(b.clear())
print(b)