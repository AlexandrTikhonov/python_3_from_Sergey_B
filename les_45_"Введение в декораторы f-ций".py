import time

# def func_decorator(func):
#     def wrapper():
#         print("----- что-то делаем перед вызовом f-ции -----")
#         func()
#         print("----- что-то делаем после вызова f-ции -----")
#
#     return wrapper
#
#
# def some_func():
#     print("Вызов f-ции some_func")
#
#
# # f = func_decorator(some_func)                 # <-- преобразовали далее удалим
# # f()
# #some_func()
#
# some_func = func_decorator(some_func)
# some_func()

# #-----------------------------
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("----- что-то делаем перед вызовом f-ции -----")
#         func(*args, **kwargs)                                      # <-- изменяем для использования нижней f-цией
#         print("----- что-то делаем после вызова f-ции -----")
#
#     return wrapper
#
#
# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag}")
#
#
# some_func = func_decorator(some_func)
# some_func("Python навсегда!", "h1")

# #-----------------------------
# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("----- что-то делаем перед вызовом f-ции -----")
#         res = func(*args, **kwargs)                                  # <-- изменяем для использования нижней f-цией
#         print("----- что-то делаем после вызова f-ции -----")
#         return res                                                   # вызов параметра
#
#     return wrapper
#
#
# def some_func(title, tag):
#     print(f"title = {title}, tag = {tag}")
#     return f"<{tag}><{title}></{tag}>"
#
#
# some_func = func_decorator(some_func)
# res = some_func("Python навсегда!", "h1")
# print(res)

#-----------------------------
def test_time(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        et = time.time()
        dt = et - st
        print(f"Время работы {dt} cek.")
        return res

    return wrapper


@test_time
def get_nod(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@test_time
def get_fast_nod(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


# get_nod = test_time(get_nod)
# get_fast_nod = test_time(get_fast_nod)

res = get_nod(2, 1000000)
res2 = get_fast_nod(2, 1000000)
print(res, res2)
