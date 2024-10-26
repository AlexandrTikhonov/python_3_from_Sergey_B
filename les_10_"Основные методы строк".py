# s = "python"
# print(type(s))
#
# # объект.метод(аргументы)
# s_1 = s.upper()                                         # upper()
# s_2 = s_1.lower()                                       # lower()
#
# print(s)
# print(s_1)
# print(s_2)

#-------------------------------------
# String.count(sub[,start[, end]]                          # count()
# start - индекс, с которого начинается поиск;
# end - индекс, которым заканчивается поиск.

msg = 'abrakadabra'

# print(msg.count("ra"))

#-----------------------------------------
# String.find(sub[,start[, end]]                            # find()
# start - индекс, с которого начинается поиск;
# end - индекс, которым заканчивается поиск.

# print(msg.find('br'))
# print(msg.rfind('br'))

#-----------------------------------------
# String.index(sub[,start[, end]]                            # index()
# start - индекс, с которого начинается поиск;
# end - индекс, которым заканчивается поиск.

# print(msg.index('br'))
# print(msg.index('br', 2))

#----------------------------------------
# String.replace(old, new, count=-1)                          # replace()
# count - максимальное количество замен (-1 - без ограничений)

#
#--------------------------------------------
# String.isalpha()                                           # isalpha()
# String.isdigit()                                           # isdigit()

# print(msg.isalpha())
#
# b = '56'
# print(b.isdigit())

#--------------------------------------------
# String.rjust(width[, fillstart=''])                        # rjust()
# String.ljust(width[, fillstart=''])                        # ljust()

# d = "abc"
# print(d)
# print(d.rjust(5))
#
# d_1 = '12'
# print(d_1.rjust(4, '0'))
# print(d_1.ljust(4, '*'))

#---------------------------------------------
# String.split(sep=None, maxsplit=-1)                          # split()
# sep - фрагмент разбиения строки
# Strip.join(список)                                          # join()

# name = 'Иванов Иван Иванович'
# print(name.split(" "))

# #------------------------------------------------
# digs = '1, 2, 3,  4,5,  6'
# digs_2 = digs.replace(" ", "").split(",")
# digs_3 = "/ ".join(digs_2)
#
# print(digs_3)

# #--------------------------------------------------
# fio = ", ".join(name.split())
# print(fio)

#-----------------------------------------------------
# String.strip()                                                # strip()

words = "   Hello world   "

print(words.lstrip())
print(words.rstrip())
print(words.strip())