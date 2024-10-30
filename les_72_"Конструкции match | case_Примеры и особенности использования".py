# def connect_db(connect: dict) -> str:
#     match connect:
#         case {'server': host, 'login': login, 'password': psw, 'port': port}:
#             return f"connection: {host}@{login},{psw}:{port}"
#         case {'servet': host, 'login': login, 'password': psw}:
#             port = 22
#             return f"connection: {host}@{login},{psw}:{port}"
#         case _:
#             return "error connection"
#
#
# request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234', 'port': 24}
#
# res = connect_db(request)
# print(res)

# # ----------------------------------
# def connect_db(connect: dict) -> str:
#     match connect:
#         case {'server': host, 'login': login, 'password': psw, 'port': port}:
#             pass
#         case {'servet': host, 'login': login, 'password': psw}:
#             port = 22
#         case _:
#             return "error connection"
#
#     return f"connection: {host}@{login},{psw}:{port}"
#
#
# request = {'server': '127.0.0.1', 'login': 'root', 'password': '1234', 'port': 24}
#
# res = connect_db(request)
# print(res)

# --------------------------------
import consts

cmd = 5

match cmd:
    case consts.CMD_3:
        print("3")
    case consts.CMD_5:
        print("5")
