# print("Запуск цикла")
#
# i = 0
# while True:
#     i += 1
#     break
#
# print("Завершение цикла")

# #-------------------------
# d = [1, 5, 3, 6, 0, -4]
#
# flFind = False
# i = 0
# while i < len(d):
#     # print(i)
#     flFind = d[i] % 2 == 0
#     if flFind:
#         break
#
#     i += 1
#
# print(flFind)

# #-------------------------------
# s = 0
# d = 1
#
# while d != 0:
#     d = int(input("Введите целое число: "))
#     if d % 2 == 0:
#         continue
#
#     s += d
#     print("s = " + str(s))

#----------------------------------
s = 0
i = -10

while i < 0: # если
    if i == 0:
        break
    s += 1/i
    i += 1
else:
    print("Сумма вычислена корректно")

print(s)