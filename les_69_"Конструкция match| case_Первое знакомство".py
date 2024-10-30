cmd = 7

# match cmd:
#     case 'top':
#         print("вверх")
#     case 'left':
#         print("влево")
#     case 'right':
#         print("вправо")
#     case _:    # wildcard
#         print("другое")
#
# print("проверки завершены")

# # --------------
# match cmd:
#     case 'top' | 'left' | 'right':
#         print("было движение")
#     case _:    # wildcard
#         print("другое")
#
# print("проверки завершены")

# # ---------------------
# match cmd:
#     case "right":
#         print("right")
#     case command:                       # равносильно --> command == cmd
#         print(f"команда: {command}")

# # ---------------------
# match cmd:
#     case "right":
#         print("right")
#     case _:
#         print(f"другая команда")

# ---------------------
match cmd:
    case str() as command:                             # равносильно case str(command)
        print(f"строковая команда: {command}")
    case bool() as command:
        print(f"булева команда: {command}")
    case int() as command if 0 <= command <= 9:
        print(f"целочисленная команда: {command}")


    case _:                                # wildcard
        print(f"другая команда")

