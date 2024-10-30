# cnt: int = 0
#
# # cnt = 0             # тип int
# # msg = "Hello"       # тип str
# # lst = [1, 2, 3]     # тип list
#
# cnt = 5.6             # подчеркивает ошибку
# msg = 0

#-------------------------
# def mul2(x: int):
#     return x * 2
#
#
# print(mul2.__annotations__)
# res = mul2(5)
# print(res)

# #-------------------------
# def mul3(x: float, y: int) -> float:
#     return x * y
#
#
# print(mul3.__annotations__)
# res1 = mul3(5, 4)
# print(res1)

# ------------------------------- Union, Optional, Any, Final --------------------
from typing import Union, Optional, Any, Final

# def mul4(x: Union[int, float], y: Union[int, float] = 2) -> Union[int, float]:    # x: Union[int, float], = x:int | float
#     return x * y
#
#
# res = mul4(5, 8)
# print(mul4.__annotations__)
# print(res)

# # ------------------------
# Digit = Union[int, float]
# Str = Optional[str]
# StrType = Union[str, None]

# #-----------------------------
# def show_x(x: float, descr: Optional[str] = None) -> None:
#     if descr:
#         print(f"{descr} {x}")
#     else:
#         print(f"x = {x}")
#
#
# show_x(55.85, 'sum_ = ')
#
# # ---------------------------
# def show_y(x: Any, descr: Optional[str] = None) -> None:
#     if descr:
#         print(f"{descr} {x}")           # Any - ставим когда можно ставить любой тип данных (неопределен по условию)
#     else:
#         print(f"x = {x}")
#
#
# show_y("55.85", 'y:')

#------------------------------
MAX_VALUE: Final = 1000          # применяется для отметки констант

