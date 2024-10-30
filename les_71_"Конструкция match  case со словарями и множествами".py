# request = {'url': 'https://proproprogs.ru/', 'method': 'GET', 'timeout': 1000}

# match request:
#     case {'url': url, 'method': method}:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print("неверный запрос")

# # ---------------------
# match request:
#     case {'url': str() as url, 'method': str(method)}:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print("неверный запрос")

# # -----------------------
# match request:
#     case {'url': url, 'method': method} if len(request) <= 3:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print("неверный запрос")

# # -----------------------
# match request:
#     case {'url': url, 'method': method, **kwargs} if not kwargs:
#         print(f"Запрос: url: {url}, method: {method}")
#     case _:
#         print("неверный запрос")

# # -------------------------------------
# json_data = {'id': 2, 'type': 'list', 'data': [1, 2, 3], 'access': True, 'date': '01.01.2023'}
#
# match json_data:
#     case {'type': 'list', 'data': list() as lst}:
#         print(f"JSON-данные: type-list: {lst}")
#     case _:
#         print("неверный запрос")

# # --------------------------------
# json_data = {'id': 2, 'access': True, 'info': ['01.01.2023', {'login': '123', 'email': 'email@m.ru'}, True, 1000]}
#
# match json_data:
#     case {'access': access, 'info': [_, {'email': email}, _, _]}:
#         print(f"JSON: access: {access}, email: {email}")
#     case _:
#         print("неверный запрос")

# ------------------------------------
primary_keys = {1, 2, 3}

match primary_keys:
    case set() as keys if len(keys) == 3:
        print(f"Primary_keys: {keys}")
    case _:      # wildcard
        print("неверный запрос")