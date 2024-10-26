# def get_V(a, b, c):
#     print(f"a = {a}, b = {b}, c = {c}")
#     return a * b * c
#
#
# v = get_V(1, 2, 3)
# print(v)
#
# v_1 = get_V(b=1, c=2, a=3)
# print(v_1)
#
# v_2 = get_V(5, b=2, c=3)
# print(v_2)
from os import lstat


# #-------------------------------------------------------
# def get_V1(a, b, c, verbose=True):
#     if verbose:
#         print(f"a = {a}, b = {b}, c = {c}")
#
#     return a * b * c
#
#
# v_3 = get_V1(5, 4, 6, False)
# print(v_3)

# #-------------------------------------------------
# def cmp_str(s1, s2, reg=False, trim=True):
#     if reg:
#         s1 = s1.lower()
#         s2 = s2.lower()
#     if trim:
#         s1 = s1.strip()
#         s2 = s2.strip()
#
#     return s1 == s2
#
#
# print(cmp_str("Python ", " Python"))

# #------------------------------------------------------
# def add_value(value, lst=[]):
#     lst.append(value)
#     return lst
#
#
# l = add_value(1)
# l = add_value(2)
# print(l)

#--------------------------------------------------------
def add_value_1(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst


l = add_value_1(1)
l = add_value_1(2, l)
print(l)