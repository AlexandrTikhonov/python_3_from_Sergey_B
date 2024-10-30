from __future__ import annotations
from typing import Type, TypeVar


# tr: dict = {'car': 'машина'}
#
# x: object = None
# x = 123
# x ='123'
#
# class Geom: pass
# class Line: pass
#
#
# g: Geom
# g = Line()
#
# ----------------------------------------
# # Any object
# # Тип Any совместим с любым другим типом, а object - ни с каким другим

# a: Any = None
# s: str
#
# s = a

# a: Any = None
# s: str
#
# s = a

# # --------------
# class Geom: pass
#
#
# class Point2D: pass
#
#
# T = TypeVar("T")                    #  <-- обобщенные тип без ограничений
# T1 = TypeVar("T1", bound=Geom)        # использование базового класса Geom
# T2 = TypeVar("T2", int, float)
#
#
# def factory_object(cls_obj: Type[T]) -> T:
#     return cls_obj()
#
#
# geom: Geom = factory_object(Geom)
# point: Point2D = factory_object(Point2D)

#------------------------------------
class Geom: pass


class Point2D(Geom):
    x: int
    y: int


    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


    def copy(self) -> Point2D:
        return Point2D(self.x, self.y)


p = Point2D(10, 20)
