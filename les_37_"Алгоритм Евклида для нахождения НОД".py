import time

def get_not(a, b):
    """
    Вычисляется НОД для натуральных чисел a и b
    по алгоритму Евклида.
    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """
    # while a != b:                                  # начальное решение (медленное)
    #     if a > b:
    #         a -= b
    #     else:
    #         b -= a
    #
    # return a


    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b

    return a

def test_nod(func):
    # --- тест №1 ----------------------
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test1 - ok')
    else:
        print('test1 - fail')


    # --- тест №2 ----------------------
    a = 100
    b = 1
    if res == 1:
        print('test2 - ok')
    else:
        print('test2 - fail')


    # --- тест №3 ---------------------------
    a = 2
    b = 10000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('#test3 - ok')
    else:
        print('#test3 - fail')
test_nod(get_not)