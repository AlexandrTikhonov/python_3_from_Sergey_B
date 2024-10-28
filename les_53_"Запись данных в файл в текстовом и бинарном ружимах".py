import pickle

# try:
#     with open("out.txt", "a") as file:
#         file.write("Hello1\n")
#         file.write("Hello2\n")
#         file.write("Hello3\n")
# except:
#     print("Ошибка при работе с файлом")

#--------------
# try:
#     with open("out.txt", "a") as file:
#         file.seek(0)
#         file.writelines("hello1\nhello2\nhello3\n")
#         file.write("hello4\n")
#         s = file.readlines()
#         print(s)
# except:
#     print("Ошибка при работе с файлом")

# #---------------
# books = [
#     ("Евгений Онегин", "Пушкин А.С.", 200),
#     ("Муму", "Тургеньев И.С.", 250),
#     ("Мастер и Маргарита", "Булгаков М.А.", 500),
#     ("Мертвые души", "Гоголь Н.В.", 190)
# ]
#
# # file = open("out.bin", "wb")           # команды на запись
# # pickle.dump(books, file)
# # file.close
#
# file = open("out.bin", "rb")            # команды на чтение
# bs = pickle.load(file)
# file.close()
# print(bs)

# #----------------------
# books1 = ["Евгений Онегин", "Пушкин А.С.", 200]
# books2 = ["Муму", "Тургеньев И.С.", 250]
# books3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
# books4 = ["Мертвые души", "Гоголь Н.В.", 190]
#
# try:
#     with open("out.bin", "wb") as file:
#         pickle.dump(books1, file)
#         pickle.dump(books2, file)
#         pickle.dump(books3, file)
#         pickle.dump(books4, file)
# except:
#     print("Ошибка при работе с файлом")

#---------------------------
#----------------------
books1 = ["Евгений Онегин", "Пушкин А.С.", 200]
books2 = ["Муму", "Тургеньев И.С.", 250]
books3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
books4 = ["Мертвые души", "Гоголь Н.В.", 190]

try:
    with open("out.bin", "rb") as file:
        b1 = pickle.load(file)
        b2 = pickle.load(file)
        b3 = pickle.load(file)
        b4 = pickle.load(file)
except:
    print("Ошибка при работе с файлом")

print(b1, b2, b3, b4, sep="\n")