# def get_sqrt(x):
#     res = None if x < 0 else x ** 0.5
#     return res
#
#
# a = get_sqrt(49)
# print(a)

# #----------------------------------
# def get_sqrt_1(x):
#     res = None if x < 0 else x ** 0,5
#     return res, x
#
#
# a, b = get_sqrt_1(49)
# print(a, b)

# #---------------------------------------
# def get_max2(a, b):
#     return a if a > b else b
#
#
# x, y = 5, 7
# print(get_max2(x, y))

#---------------------------------------
# def get_max2(a, b):
#     return a if a > b else b


# x, y, z = 5, 7, 10
# print(get_max2(x, get_max2(y, z)))

#---------------------------------------
# def get_max3(a, b, c):
#     return get_max2(a, get_max2(b, c))
#
#
# x, y, z = 5, 7, 10
# print(get_max3(x, y, z))

#--------------------------------------
# PERIMETR = True                    # меняя значение True на False получаем периметр или площадь прямоугольника
# if PERIMETR:
#     def get_rect(a, b):
#         return 2 * (a + b)
# else:
#     def get_rect(a, b):
#         return a * b
#
# print(get_rect(1.5, 3.8))

#----------------------------------
# f-ция возвращает четное число
def even(x):
    return x % 2 == 0


for i in range(1, 20):
    if even(i):
        print(i)