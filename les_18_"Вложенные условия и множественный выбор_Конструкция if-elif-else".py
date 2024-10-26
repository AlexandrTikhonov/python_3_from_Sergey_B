# x = int(input())
#
# if x % 2 == 0:
#     if 0 <= x <= 9:
#         print("x - цифра")
#     else:
#         print("x - число")
# else:
#     print("x - нечетное число")

# #---------------------------
# a, b, c = 5, 12, 8
#
# if a > b:
#     if a > c:
#         print("a - максимальное число")
#     else:
#         print("c - максимальное число")
# else:
#     if b > c:
#         print("b - максимальное число")
#     else:
#         print("c - максимальное число")

# #------------------------------
# """
# дан список курсов по программированию, необходимо выбрать нужный курс
# 1. Python
# 2. C++
# 3. Java
# 4. JavaScript
# """
#
# item = int(input())
#
# if item == 1:
#     print("Выбран курс по Python")
# elif item == 2:
#     print("Выбран курс по С++")
# elif item == 3:
#     print("Выбран курс по Java")
# elif item == 4:
#     print("Выбран курс по JavaScript")
# else:
#     print("Неверный пункт")

#-----------------------------
x = int(input())

if x < 0:
    print("x должно быть положительным")
elif 0 <= x <= 9:
    print("x - цифра")
elif 10 <= x <= 99:
    print("x - двухзначное число")
elif 100 <= x <= 999:
    print("x - трехзначное число")

