# n = int(input("Введите натуральное число не более 100: "))
#
# if n < 1 or n > 100:
#     print("Неверное число")
# else:
#     p = 1
#     for i in range(1, n+1):
#         p *= i
#
#     print(f"Факториал {n} = {p} ")

# #------------------------------------
# for i in range(1, 7):
#     print("*" * i)

# #------------------------------------
# words = ["Python", "дай", "мне", "силы", "пройти", "этот", "курс", "до", "конца"]
#
# # s = ""
# #
# #  for word in words:
# #     s += " " + word
#
# s = " ".join(words)
#
# print(s.lstrip())

# #-----------------------------------
# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# # for i in range(len(digs)):
# #     if 10 <= abs(digs[i]) <= 99:
# #         digs[i] = 0
#
# for i, d in enumerate(digs):
#     if 10 <= abs(d) <= 99:
#         digs[i] = 0
#
# print(digs)

# -----------------------------------
t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o',
     'r', 's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shch', '', 'ee', 'yu', 'ya']

start_index = ord('a')
title = "Программирование на Python - лучший курс"
slug = ''

for s in title.lower():
    if 'а' <= s <= 'я':
        slug += t[ord(s) - start_index]
    elif s == 'ё':
        slug += 'yo'
    elif s in '!?;:.,':
        slug += '-'
    else:
        slug += s
