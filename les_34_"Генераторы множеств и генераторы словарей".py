# a = {x ** 2 for x in range(1, 5)}
# print(a)
#
# b = {x: x ** 2 for x in range(1, 5)}
# print(b)

# #-----------------------------------
# # Преобразовать список во множество
# d = [1, 2, "1", "2", -4, 3, 4]
# mn = {int(x) for x in d}
# print(mn)

# #----------------------------------
# # Есть словарь, записать ключи с заглавной буквы, а все значения превратить в числа
# d = {"неуд.": 2, "уд.": 3, "хор": 4, "отл.": 5}
# a = {key.upper(): int(value) for key, value in d.items()}
# print(a)

# #----------------------------------
# d = [1, 2, '1', '2', -4, 3, 4]
# a = {int(x) for x in d if int(x) > 0}
# print(a)

#-----------------------------------
m = {'безнадежно': 0, 'убого': 1, 'неудовлетворительно': 2, 'удовлетворительно': 3, 'хорошо': 4, 'отлично': 5}
a = {int(value): key for key, value in m.items() if 2 <= int(value) <= 5}
print(a)