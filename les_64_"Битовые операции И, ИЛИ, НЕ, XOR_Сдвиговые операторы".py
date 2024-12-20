# ## нижнее выражение автоматически загрузилось при создании модуля !!!
#
# # import unittest
# #
# #
# # class MyTestCase(unittest.TestCase):
# #     def test_something(self):
# #         self.assertEqual(True, False)  # add assertion here
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
# # ----------------------------  Битовая операция НЕ   -----------------
# #    таблица
# # X | HE |
# # 0 | 1  |
# # 1 | 0  |
#
# a = 121
# print(bin(a)) # --> 0b1111001
# print(~a)     # --> -122
#
# d = 0
# print(~d)     # --> -1
#
# d1 = -10
# print(~d1)    # --> 9
#
# # --------------------------   Битовая операция И   ---------------
# #    &  - амперсанд
#
# #   таблица
# # x1 | x2 | И |
# #  0 |  0 | 0 | --> 0
# #  0 |  1 | 0 | --> 0
# #  1 |  0 | 0 | --> 0
# #  1 |  1 | 1 | --> 1

# flags = 5
# mask = 4
#
# if flags & mask == mask:
#     print("Включен 2-й бит числа")
# else:
#     print("2-й бит выключен")

# # -----------------------
# flags = 13
# mask = 5
#
# flags = flags & ~mask
# print(flags)           # --> 8

# ----------------------      Битовая операция ИЛИ    -----
# #   таблица
# # x1 | x2 |ИЛИ|
# #  0 |  0 | 0 |
# #  0 |  1 | 1 |
# #  1 |  0 | 1 |
# #  1 |  1 | 1 |

# # -----------------------
# flags = 8
# mask = 5
#
# flags |= mask   # --> равносильно -->  flags = flags | mask
# print(flags)           # --> 13

# -----------------------    Битовая операция XOR
##     ^ XOR  "КСОР"
# #   таблица
# # x1 | x2 |XOR|
# #  0 |  0 | 0 | --> 0
# #  0 |  1 | 1 | --> 0
# #  1 |  0 | 1 | --> 0
# #  1 |  1 | 0 | --> 1

# # -----------------------
# flags = 9
# mask = 1
#
# flags = flags ^ mask
# flags = flags ^ mask             # повторное включение команды вернет начальное значение
# print(flags)           # --> 8


# -------------------------- СДВИГ БИТ КОМАНДАМИ >> or <<
a = 160
print(bin(a)) # --> 0b10100000

a = a >> 1
print(bin(a)) # -- >0b1010000
print(a)      # --> 80

a = a >> 2
print(bin(a)) # -- >0b10100
print(a)      # --> 20

a = a >> 2
print(bin(a)) # -- >0b101
print(a)      # --> 5

a = a >> 1
print(bin(a)) # -- >0b10
print(a)      # --> 2

a = a << 1
print(a)      # --> 4                   ПРОСТО ОПЕРАЦИЯ УМНОЖЕНИЕ НА 2, если значение >> 1

a = a << 2
print(a)      # --> 16                  ПРОСТО ОПЕРАЦИЯ УМНОЖЕНИЕ НА 4, если значение >> 2