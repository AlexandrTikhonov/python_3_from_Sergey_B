# N = 1000
# s = 0
# i = 0

# while i <= N:
#     s += i
#     i += 1
#     print(i)
#     #print(s)

# #-------------------------
# while i < 10:
#     i += 1
#     s += i
#     print(i)
#
# print(s)

#---------------------------
# pass_true = 'password'
# ps = ''
#
# while ps != pass_true:
#     ps = input("Введите пароль: ")
#
# print("Вход в систему")

#---------------------------
n = 20
i = 1
char = []

while i < n:
    if i % 3 == 0:
        char.append(i)
    i += 1

print(char)
