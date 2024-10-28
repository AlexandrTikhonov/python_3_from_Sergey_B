# try:
#     file = open('pyproject.toml', encoding='utf-8')
#     s = file.readlines()
#     print(s)
#     file.close()
# except FileNotFoundError:
#     print("Невозможно открыть файл")

#---------------------------
try:
    with open("pyproject.toml", encoding="utf-8") as file:
        s = file.readlines()
        print(s)

    # file = open('pyproject.toml', encoding='utf-8')
    # try:
    #     s = file.readlines()
    #     int(s)
    #     print(s)
    # finally:
    #     file.close()
except FileNotFoundError:
    print("Невозможно открыть файл")
except:
    print("Ошибка при работе с файлом")