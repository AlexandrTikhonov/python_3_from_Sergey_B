cmd = ("Пушкин А.С.", "Руслан и Людмила", 220)
cmd = [1, "Пушкин А.С.", "Руслан и Людмила", 220, 2023]

# match cmd:
#     case tuple() as book:
#         print(f"кортеж: {book}")
#     case _:
#         print("непонятный формат данных")

# # ----------------------------------
# match cmd:
#     case author, title, pages:
#         print(f"Книга: {author}, {title}, {pages}")
#     case _:
#         print("непонятный формат данных")

# ----------------------------------
# match cmd:
#     case (author, title, pages, *_) if len(cmd) < 6:  # *_ применяется для распаковки несколько неопределенных данных
#         print(f"Книга: {author}, {title}, {pages}")
#     case _:
#         print("непонятный формат данных")

# # ----------------------------------
# match cmd:
#     case (str() as author, str() as title, int() | float() as pages, *_) if len(cmd) < 6:
#         print(f"Книга: {author}, {title}, {pages}")
#     case _:
#         print("непонятный формат данных")

# # ----------------------------------
# match cmd:
#     case (author, title, pages):
#         print(f"Книга1: {author}, {title}, {pages}")
#     case[_, author, title, pages, _]:                        # ==> case[_, author, title, pages, year]:
#         print(f"Книга2: {author}, {title}, {pages}")         #     print(f"Книга2: {author}, {title}, {pages}, {year}")
#     case _:
#         print("непонятный формат данных")

# # ----------------------------------
# match cmd:
#     case (author, title, pages) | [_, author, title, pages, _]:
#         print(f"Книга: {author}, {title}, {pages}")
#     case _:
#         print("непонятный формат данных")

# ----------------------------------
match cmd:
    case tuple():
        print("Неверный формат данных кортеж")
    case (author, title, pages) | [_, author, title, pages, _]:
        print(f"Книга: {author}, {title}, {pages}")
    case[_, author, title, pages, year]:
        print(f"Книга2: {author}, {title}, {pages}, {year}")
    case _:
        print("непонятный формат данных")