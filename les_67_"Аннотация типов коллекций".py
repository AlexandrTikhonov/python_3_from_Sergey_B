from typing import Callable
# from typing import list, Tuple, Dict, Set

# lst: List[int] = [1, 2, 3]

# addr: tuple[int, str]

# book: tuple[str, str, int]
# book: ("Пушкин А.С.", "Руслан и Людмила", 225)
#
# elems: tuple[float, ...]
# elems: (1.0, )
# elems: (1.0, 2.0)

# words: dict[srt, int] = {'one' : 1, 'two' : 2}

# persons: set[str] = {'dshf','sfsg', 'fgsa'}

# #---------------------------
# def get_positive(digits: list[int | float]) -> list[int | float]:
#     return list(filter(lambda x: x > 0, digits))
#
#
# print(get_positive([1, -2, 3.5, 4, 5]))

# #------------------------------
# def get_digits(flt, lst):
#     if lst is None:
#         return []
#     return list(filter(flt, lst))
#
#
# print(get_digits(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#------------------------------
def get_digits(flt: Callable[[int], bool], lst: list[int] = None) -> list[int]:
    if lst is None:
        return []
    return list(filter(flt, lst))

def even(x: int):
    return bool(x % 2 == 0)


print(get_digits(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
