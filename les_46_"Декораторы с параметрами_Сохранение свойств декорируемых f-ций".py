from functools import wraps
import math


# def func_decorator(func):
#     def wrapper(x, *args, **kwargs):
#         dx = 0.0001
#         res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#         return res
#
#     return wrapper
#
#
# @func_decorator
# def sin_df(x):
#     return math.sin(x)
#
#
# df = sin_df(math.pi/3)
# print(df)

# ----------------------------------
# def df_decorator(dx=0.01):
#     def func_decorator(func):
#         def wrapper(x, *args, **kwargs):
#             res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
#             return res
#
#         return wrapper
#
#     return func_decorator
#
#
# # @df_decorator(dx=0.01)                       # декоратор
# def sin_df(x):
#     return math.sin(x)
#
#
# # f = df_decorator(dx=0.01)                    # запись декоратора другим способом
# # sin_df = f(sin_df)
#
# sin_df = df_decorator(dx=0.01)(sin_df)         # запись декоратора еще 1 способом в 1 строку
#
# df = sin_df(math.pi / 3)
# print(df)

# ----------------------------
def df_decorator(dx=0.01):
    def func_decorator(func):
        @wraps(func)
        def wrapper(x, *args, **kwargs):
            res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
            return res

        wrapper.__name__ = func.__name__        # 3. данная запись оставляет возможность не изменять имя f-ции
        wrapper.__doc__ = func.__doc__

        return wrapper

    return func_decorator

# @df_decorator(dx=0.01)                          # 2. декоратор, изменяющий имя f-ции
def sin_df(x):
    """Функция для вычисления производной синуса"""
    return math.sin(x)


print(sin_df.__name__)                          # 1. вывод имени f-ции в консоль без 3 шага

print(sin_df.__doc__)                             # 5. вывод __doc__ с использованием декоратора





6